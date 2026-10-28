#!/usr/bin/env python3
"""Validate synthetic slice fixtures. Does NOT run or simulate Godot gameplay."""
import copy
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "prototype" / "first-playable"

def require(ok, message):
    if not ok:
        raise ValueError(message)

def integer(value, low, high=None):
    return type(value) is int and value >= low and (high is None or value <= high)

def unique(values):
    return len(values) == len(set(values))

def validate(d, s):
    require(d["format_version"] == 1 and d["public_fixture"] is True, "definition version/public flag")
    require(s["save_version"] == 1 and s["content_version"] == d["content_version"], "save/content version")
    require(s["fixture_id"] == "prepared-community-day", "fixture isolation")
    require(d["calendar"]["days_per_season"] == 30 and d["calendar"]["seasons"] == ["spring","summer","autumn","winter"], "calendar")
    wake, cutoff = d["clock"]["wake_minute"], d["clock"]["cutoff_minute"]
    require(integer(wake,0,1439) and integer(cutoff,wake+1,1440), "clock bounds")
    require(d["clock"]["seconds_per_game_minute"] > 0, "clock speed")
    for group in ["items","crops","npcs","events"]:
        require(unique([x["id"] for x in d[group]]), "duplicate " + group + " id")
    items = {x["id"]: x for x in d["items"]}
    crops = {x["id"]: x for x in d["crops"]}
    npcs = {x["id"]: x for x in d["npcs"]}
    events = {x["id"]: x for x in d["events"]}
    locations = set(d["locations"])
    require(len(locations) == len(d["locations"]), "duplicate location")
    for item in items.values():
        require(item["kind"] in ["seed","produce"], "item kind")
        if item["kind"] == "seed":
            require(integer(item["price"],0), "price")
    for c in crops.values():
        require(c["seed_id"] in items and items[c["seed_id"]]["kind"] == "seed", "crop seed reference")
        require(c["harvest_id"] in items and integer(c["watered_nights"],1) and integer(c["yield"],1), "crop growth/yield")
    for n in npcs.values():
        previous = wake
        for interval in n["schedule"]:
            require(interval["start"] == previous and integer(interval["end"],previous+1,cutoff), "schedule gap/overlap")
            require(interval["location"] in locations, "schedule location")
            previous = interval["end"]
        require(previous == cutoff, "schedule coverage")
    for o in d["schedule_overrides"]:
        require(o["npc_id"] in npcs and o["location"] in locations, "override reference")
        require(wake <= o["start"] < o["end"] <= cutoff, "override window")
        require(set(o["requires_flags"] + o["unless_flags"]) <= set(d["flags"]), "override flags")
    known_effects = {
        "record_contact","set_helper_chat","pay_job","set_helper_job_done","add_job_category",
        "take_mint","add_herb_stock","add_supply_category","pay_shift","add_service_category",
        "set_helper_visit_eligible","repair_gate","set_neighbor_invitation_available"
    }
    for e in events.values():
        require(e["actor"] in npcs and (e["location"] in locations or e["location"] == "any"), "event actor/location")
        start, end = e["window"]
        require(wake <= start < end <= cutoff and integer(e["duration"],0,end-start), "event duration/window")
        require(set(e["depends_on"]) <= set(events), "unknown dependency")
        require(set(e["effects"]) <= known_effects, "unknown effect")
        require(e["repeat"] in ["once","daily_contact","transaction","daily_completion"], "repeat policy")
        require(e.get("condition") in [None,"two_distinct_categories"], "unknown condition")
    visited, visiting = set(), set()
    def visit(key):
        require(key not in visiting, "event dependency cycle")
        if key in visited:
            return
        visiting.add(key)
        for dependency in events[key]["depends_on"]:
            visit(dependency)
        visiting.remove(key)
        visited.add(key)
    for key in events:
        visit(key)
    v = d["venue"]
    require(v["shift_latest_start"] + v["shift_minutes"] == v["close"], "latest shift start")
    require(v["contribution_item"] in items and integer(v["servings_per_contribution"],1), "menu reference")
    require(v["shift_minutes"] == events["FP_SHIFT"]["duration"], "shift duration mismatch")
    require(v["orders"] == 3 and unique([r["id"] for r in v["recipes"]]), "recipes/orders")
    day, minute = s["clock"]["absolute_day"], s["clock"]["minute_of_day"]
    require(integer(day,0) and integer(minute,wake,cutoff), "saved date/time")
    require(0 <= s["clock"]["subminute"] < d["clock"]["seconds_per_game_minute"], "subminute")
    require(s["player"]["scene"] in locations and integer(s["player"]["coins"],0), "player scene/coins")
    import math
    require(len(s["player"]["position"]) == 2 and all(type(x) in (int,float) and math.isfinite(x) for x in s["player"]["position"]), "position")
    require(len(s["inventory"]) <= d["inventory"]["slots"], "inventory capacity")
    for stack in s["inventory"]:
        require(stack["item_id"] in items and integer(stack["quantity"],1,d["inventory"]["stack_limit"]), "inventory stack")
    farm = s["farm"]
    require(integer(farm["can_charges"],0,d["farm"]["can_capacity"]), "water capacity")
    require(farm["last_processed_day"] == day-1, "overnight processing marker")
    require(len(farm["plots"]) == d["farm"]["plot_count"] and unique([p["id"] for p in farm["plots"]]), "plot identity/count")
    for p in farm["plots"]:
        require(type(p["tilled"]) is bool and type(p["watered"]) is bool, "plot booleans")
        if p["crop_id"] is None:
            require(p["growth"] == 0 and not p["watered"], "empty plot state")
        else:
            require(p["crop_id"] in crops and p["tilled"], "planted crop reference")
            require(integer(p["growth"],0,crops[p["crop_id"]]["watered_nights"]), "growth bound")
    require(set(s["npcs"]) == set(npcs) and set(s["relationships"]) == set(npcs), "resident state coverage")
    for state in s["npcs"].values():
        require(state["anchor"] in locations and state["destination"] in locations, "saved NPC anchor")
    for r in s["relationships"].values():
        require(type(r["met"]) is bool and r["romance"] == "none", "public fixture relationship")
        require(unique(r["contact_days"]) and all(integer(x,0,day) for x in r["contact_days"]), "contact days")
        require(unique(r["evidence"]) and all(isinstance(x,str) for x in r["evidence"]), "evidence")
    for pair, state in s["pair_relationships"].items():
        parts = pair.split("|")
        require(len(parts) == 2 and parts == sorted(parts) and len(set(parts)) == 2 and set(parts) <= set(npcs), "pair key")
        require(isinstance(state,str) and bool(state), "pair state")
    require(set(s["flags"]) == set(d["flags"]) and all(type(x) is bool for x in s["flags"].values()), "saved flags")
    categories = s["community"]["categories"]
    require(unique(categories) and set(categories) <= set(d["standing"]["categories"]), "standing categories")
    expected = "neighbor" if len(categories) >= d["standing"]["neighbor_distinct_categories"] else "newcomer"
    require(s["community"]["stage"] == expected, "derived standing")
    require(integer(s["venue"]["herb_stock"],0), "venue stock")
    require(unique(s["completed_events"]) and set(s["completed_events"]) <= set(events), "completed IDs")
    require(unique(s["transactions"]) and all(isinstance(x,str) and x for x in s["transactions"]), "transaction IDs")
    for event_id, days in s["daily_records"].items():
        require(event_id in events and unique(days) and all(integer(x,0,day) for x in days), "daily records")
    require(len(s["visits"]) <= 1, "visitor slot")
    for reservation in s["visits"]:
        require(reservation["npc_id"] in npcs and integer(reservation["day"],day), "visit reference/day")
        require(wake <= reservation["start"] < reservation["end"] <= cutoff, "visit window")
    a = s["active_activity"]
    if a is not None:
        require(a["event_id"] in events, "active event reference")
        e = events[a["event_id"]]
        require(e["kind"] in ["job","shift","favor","invitation"], "active event kind")
        require(isinstance(a["instance_id"],str) and bool(a["instance_id"]) and type(a["committed"]) is bool, "active identity")
        require(a["day"] == day and minute == a["start_minute"], "active clock")
        require(a["end_minute"] == minute+e["duration"] and e["window"][0] <= minute and a["end_minute"] <= e["window"][1], "active time reservation")
        require(integer(a["step_index"],0) and integer(a["reserved_herb"],0), "active progress")
        if e["kind"] == "shift":
            require(len(a["orders"]) == v["orders"] and a["step_index"] <= v["orders"], "active order count")
            require(set(a["orders"]) <= {r["id"] for r in v["recipes"]} and a["orders"].count("herb_drink") <= 1, "active recipe")
            require(a["reserved_herb"] == a["orders"][a["step_index"]:].count("herb_drink") and not a["placements"], "reservation conservation")
        elif e["kind"] == "job":
            require(not a["orders"] and a["reserved_herb"] == 0 and unique(a["placements"]) and set(a["placements"]) <= {"spot_a","spot_b","spot_c"} and a["step_index"] == len(a["placements"]), "active job state")
        else:
            require(not a["orders"] and not a["placements"] and a["reserved_herb"] == 0 and a["step_index"] == 0, "active invitation/favor state")
        require(a["committed"] or a["step_index"] == 0, "uncommitted progress")
    return True

def self_test(d, s):
    cases = [
        ("unknown seed", lambda x,y: x["crops"][0].update(seed_id="missing")),
        ("duplicate NPC", lambda x,y: x["npcs"].append(copy.deepcopy(x["npcs"][0]))),
        ("schedule gap", lambda x,y: x["npcs"][0]["schedule"][1].update(start=541)),
        ("unknown dependency", lambda x,y: x["events"][0]["depends_on"].append("missing")),
        ("dependency cycle", lambda x,y: x["events"][0]["depends_on"].append("FP_VISIT_UNLOCK")),
        ("long activity", lambda x,y: x["events"][1].update(duration=200)),
        ("unknown effect", lambda x,y: x["events"][0]["effects"].append("invented")),
        ("negative money", lambda x,y: y["player"].update(coins=-1)),
        ("stack overflow", lambda x,y: y["inventory"][0].update(quantity=100)),
        ("unknown crop", lambda x,y: y["farm"]["plots"][0].update(crop_id="missing")),
        ("double overnight marker", lambda x,y: y["farm"].update(last_processed_day=7)),
        ("duplicate reward receipt", lambda x,y: y.update(transactions=["same","same"])),
        ("wrong standing", lambda x,y: y["community"].update(stage="neighbor")),
        ("negative stock", lambda x,y: y["venue"].update(herb_stock=-1)),
        ("future save", lambda x,y: y.update(save_version=2)),
        ("future contact", lambda x,y: y["relationships"]["resident_helper"]["contact_days"].append(8)),
        ("unknown pair", lambda x,y: y["pair_relationships"].update({"missing|resident_helper":"acquainted"})),
        ("too many visitors", lambda x,y: y.update(visits=[{},{}])),
    ]
    for name, mutate in cases:
        x, y = copy.deepcopy(d), copy.deepcopy(s)
        mutate(x,y)
        try:
            validate(x,y)
        except ValueError:
            continue
        raise AssertionError("Did not reject: " + name)
    mid = copy.deepcopy(s)
    mid["clock"]["minute_of_day"] = 720
    mid["venue"]["herb_stock"] = 2
    mid["active_activity"] = {
        "event_id":"FP_SHIFT","instance_id":"shift:7:0","day":7,
        "start_minute":720,"end_minute":840,"committed":False,
        "step_index":0,"reserved_herb":1,
        "orders":["herb_drink","house_drink","house_drink"],"placements":[]
    }
    validate(d,mid)
    consumed = copy.deepcopy(mid)
    consumed["active_activity"].update(committed=True,step_index=1,reserved_herb=0)
    validate(d,consumed)
    bad = copy.deepcopy(mid)
    bad["active_activity"]["reserved_herb"] = 0
    try:
        validate(d,bad)
    except ValueError:
        pass
    else:
        raise AssertionError("Did not reject missing stock reservation")
    # Serializing synthetic state must not mutate it or discard active reservations.
    require(json.loads(json.dumps(consumed)) == consumed, "JSON roundtrip")
    print("PASS: initial + 2 midshift snapshots; 19 invalid mutations rejected; JSON roundtrip")
    print("NOT TESTED: Godot runtime, gameplay transitions, save-file atomicity, visuals or human play")

def main():
    try:
        d = json.loads((DATA / "definitions.json").read_text())
        s = json.loads((DATA / "prepared-save.json").read_text())
        validate(d,s)
        if "--self-test" in sys.argv:
            self_test(d,s)
        else:
            print("PASS: fixture structure, references, schedules and dependency graph")
    except (ValueError,KeyError,TypeError,OSError) as exc:
        print("FAIL:", exc, file=sys.stderr)
        return 1
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

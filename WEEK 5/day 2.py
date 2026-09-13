response = {
    "status": "success",
    "user": {
        "id": 42,
        "name": "Kevin Mwangi",
        "location": {
            "city": "Kisumu",
            "country": "Kenya"
        }
    },
    "today": {
        "steps": 10800,
        "cold_shower": True,
        "fasting": {
            "protocol": "OMAD",
            "window_hours": 23
        },
        "workout": {
            "completed": True,
            "bench_press_kg": 90,
            "duration_minutes": 55
        }
    }
}

# Navigate layer by layer
name = response["user"]["name"]
city = response["user"]["location"]["city"]
steps = response["today"]["steps"]
protocol = response["today"]["fasting"]["protocol"]
bench = response["today"]["workout"]["bench_press_kg"]

print(f"Name:     {name}")
print(f"City:     {city}")
print(f"Steps:    {steps}")
print(f"Protocol: {protocol}")
print(f"Bench:    {bench} kg")
users = [
    {"name": "James Omondi",  "workout": {"bench_press_kg": 80, "duration_minutes": 45}},
    {"name": "Sandra Weru",   "workout": None},   # did not train today
    {"name": "Grace Achieng", "workout": {"bench_press_kg": 60, "duration_minutes": 40}},
]

for user in users:
    name = user["name"]
    workout = user["workout"]
    if workout is None:
        print(f"{name}: rest day")
    else:
        bench = workout.get("bench_press_kg", "not recorded")
        mins = workout.get("duration_minutes", "?")
        print(f"{name}: bench={bench}kg, duration={mins}min")


       # Raw API response: list of full user records
raw = [
    {"id": 1, "name": "James Omondi",  "email": "james@smp.ke", "steps": 9200,  "protocol": "OMAD", "sleep": 7.5, "active": True},
    {"id": 2, "name": "Sandra Weru",   "email": "sw@smp.ke",    "steps": 10500, "protocol": "2MAD", "sleep": 8.0, "active": True},
    {"id": 3, "name": "Patrick Njiru", "email": "pn@smp.ke",    "steps": 8100,  "protocol": "OMAD", "sleep": 6.5, "active": False},
    {"id": 4, "name": "Grace Achieng", "email": "ga@smp.ke",    "steps": 11000, "protocol": "OMAD", "sleep": 7.0, "active": True},
    {"id": 5, "name": "Brian Kamau",   "email": "bk@smp.ke",    "steps": 7400,  "protocol": "2MAD", "sleep": 9.0, "active": True},
]

# Extract only active users with name, steps, protocol
clean = [
    {
        "name": r["name"],
        "steps": r["steps"],
        "protocol": r["protocol"]
    }
    for r in raw if r["active"]
]

for record in clean:
    print(f"{record['name']:20} {record['steps']:6} steps  {record['protocol']}")



# What page 1 of a paginated API looks like
page_1 = {
    "page": 1,
    "total_pages": 3,
    "per_page": 3,
    "next_page": 2,
    "data": [
        {"name": "James Omondi",  "steps": 9200},
        {"name": "Sandra Weru",   "steps": 10500},
        {"name": "Patrick Njiru", "steps": 8100},
    ]
}

page_2 = {
    "page": 2,
    "total_pages": 3,
    "per_page": 3,
    "next_page": 3,
    "data": [
        {"name": "Grace Achieng", "steps": 11000},
        {"name": "Brian Kamau",   "steps": 7400},
        {"name": "Kevin Mwangi",  "steps": 10800},
    ]
}

# Combine pages manually
all_records = page_1["data"] + page_2["data"]
print(f"Total records collected: {len(all_records)}")
for r in all_records:
    print(f"  {r['name']}: {r['steps']} steps")






api_response = {
    "week": "2024-W47",
    "members": [
        {"name": "James Omondi",  "daily_steps": [9200, 10100, 8800, 11000, 9400, 10200, 8600]},
        {"name": "Sandra Weru",   "daily_steps": [10500, 9800, 10200, 11500, 9100, 10800, 10000]},
        {"name": "Patrick Njiru", "daily_steps": [8100, 7900, 8500, 9200, 8800, 7600, 9000]},
        {"name": "Grace Achieng", "daily_steps": [11000, 10800, 9900, 12000, 10500, 11200, 10300]},
    ]
}

print(f"Week: {api_response['week']}")
print("-" * 50)
print(f"{'Name':<20} {'Avg Steps':>10}  {'Days 10k+':>10}")
print("-" * 50)

for member in api_response["members"]:
    steps = member["daily_steps"]
    avg = round(sum(steps) / len(steps))
    days_hit = sum(1 for s in steps if s >= 10000)
    print(f"{member['name']:<20} {avg:>10,}  {days_hit:>10}")



    api_response = {
    "week": "2024-W47",
    "members": [
        {"name": "James Omondi",  "daily_steps": [9200, 10100, 8800, 11000, 9400, 10200, 8600]},
        {"name": "Sandra Weru",   "daily_steps": [10500, 9800, 10200, 11500, 9100, 10800, 10000]},
        {"name": "Patrick Njiru", "daily_steps": [8100, 7900, 8500, 9200, 8800, 7600, 9000]},
        {"name": "Grace Achieng", "daily_steps": [11000, 10800, 9900, 12000, 10500, 11200, 10300]},
    ]
}

results = []

for member in api_response["members"]:
    steps = member["daily_steps"]
    
    average = sum(steps) / len(steps)
    days_hit_10k = sum(1 for s in steps if s >= 10000)
    best_day = max(steps)
    
    results.append({
        "name": member["name"],
        "average_steps": round(average, 1),
        "days_hit_10k": days_hit_10k,
        "best_day": best_day
    })

# Print results
for r in results:
    print(f"{r['name']}:")
    print(f"  Average steps : {r['average_steps']}")
    print(f"  Days ≥ 10k    : {r['days_hit_10k']}")
    print(f"  Best day      : {r['best_day']}")
    print()

raw_members = [
    {
        "profile": {"name": "James Omondi", "city": "Nairobi"},
        "metrics": {"steps": 9200, "sleep_hours": 7.5, "bench_press_kg": 80},
        "discipline": {"cold_shower": True, "protocol": "OMAD"}
    },
    {
        "profile": {"name": "Grace Achieng", "city": "Mombasa"},
        "metrics": {"steps": 11000, "sleep_hours": 7.0, "bench_press_kg": 60},
        "discipline": {"cold_shower": False, "protocol": "OMAD"}
    },
    {
        "profile": {"name": "Brian Kamau", "city": "Kisumu"},
        "metrics": {"steps": 7400, "sleep_hours": 9.0, "bench_press_kg": 70},
        "discipline": {"cold_shower": True, "protocol": "2MAD"}
    },
]

# Flatten each nested record into one clean dict
flattened = []
for m in raw_members:
    record = {
        "name":       m["profile"]["name"],
        "city":       m["profile"]["city"],
        "steps":      m["metrics"]["steps"],
        "sleep":      m["metrics"]["sleep_hours"],
        "bench":      m["metrics"]["bench_press_kg"],
        "protocol":   m["discipline"]["protocol"],
        "cold_shower": m["discipline"]["cold_shower"],
    }
    flattened.append(record)

for r in flattened:
    shower = "yes" if r["cold_shower"] else "no"
    print(f"{r['name']}, {r['city']}: {r['steps']} steps, {r['protocol']}, shower={shower}")



# This is what the X API v2 returns when you fetch a post
# Structure: data (the post) + includes (the author details)
x_response = {
    "data": {
        "id": "2076589716036608320",
        "text": "Live by a code:\n\n* Loyalty.\n* Strength.\n* Honour.\n* Discipline.\n\nIf you stand for nothing, you fall for anything.",
        "created_at": "2026-07-14T05:30:00Z",
        "author_id": "748352990",
        "public_metrics": {
            "retweet_count": 2104,
            "reply_count":    487,
            "like_count":   11380,
            "quote_count":    319,
            "bookmark_count": 4251
        }
    },
    "includes": {
        "users": [
            {
                "id": "748352990",
                "name": "Amerix",
                "username": "amerix",
                "public_metrics": {
                    "followers_count": 1200000,
                    "following_count": 487
                }
            }
        ]
    }
}

# Parse it exactly as you have been parsing all lesson
post    = x_response["data"]
author  = x_response["includes"]["users"][0]
metrics = post["public_metrics"]

print("POST")
print(f"  Author:    @{author['username']} ({author['name']})")
print(f"  Text:      {post['text'][:60]}...")
print(f"  Posted:    {post['created_at']}")
print()
print("ENGAGEMENT")
print(f"  Likes:     {metrics['like_count']:,}")
print(f"  Retweets:  {metrics['retweet_count']:,}")
print(f"  Replies:   {metrics['reply_count']:,}")
print(f"  Bookmarks: {metrics['bookmark_count']:,}")
print()
print(f"AUTHOR: @{author['username']} has {author['public_metrics']['followers_count']:,} followers")
print(f"Read more at: https://x.com/{author['username']}")

# This is what the X API v2 returns when you fetch a post
# Structure: data (the post) + includes (the author details)
x_response = {
    "data": {
        "id": "2076589716036608320",
        "text": "Live by a code:\n\n* Loyalty.\n* Strength.\n* Honour.\n* Discipline.\n\nIf you stand for nothing, you fall for anything.",
        "created_at": "2026-07-14T05:30:00Z",
        "author_id": "748352990",
        "public_metrics": {
            "retweet_count": 2104,
            "reply_count":    487,
            "like_count":   11380,
            "quote_count":    319,
            "bookmark_count": 4251
        }
    },
    "includes": {
        "users": [
            {
                "id": "748352990",
                "name": "Amerix",
                "username": "amerix",
                "public_metrics": {
                    "followers_count": 1200000,
                    "following_count": 487
                }
            }
        ]
    }
}

# Parse it
post    = x_response["data"]
author  = x_response["includes"]["users"][0]
metrics = post["public_metrics"]

print("POST")
print(f"  Author:    @{author['username']} ({author['name']})")
print(f"  Text:      {post['text'][:60]}...")
print(f"  Posted:    {post['created_at']}")
print()
print("ENGAGEMENT")
print(f"  Likes:     {metrics['like_count']:,}")
print(f"  Retweets:  {metrics['retweet_count']:,}")
print(f"  Replies:   {metrics['reply_count']:,}")
print(f"  Bookmarks: {metrics['bookmark_count']:,}")
print()
print(f"AUTHOR: @{author['username']} has {author['public_metrics']['followers_count']:,} followers")
print(f"Read more at: https://x.com/{author['username']}")

# Calculate engagement rate
engagement_rate = (metrics["like_count"] + metrics["retweet_count"] + metrics["reply_count"]) / author["public_metrics"]["followers_count"] * 100
print(f"Engagement rate: {engagement_rate:.2f}%")




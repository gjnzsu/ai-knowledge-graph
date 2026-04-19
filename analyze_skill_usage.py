#!/usr/bin/env python3
"""
Skill Usage Analyzer
Analyzes skill usage patterns from tracking logs
"""

import json
import os
from collections import defaultdict, Counter
from datetime import datetime, timedelta
import sys

def load_usage_data(log_file):
    """Load usage data from JSONL file"""
    usage_data = []
    log_path = os.path.expanduser(log_file)

    if not os.path.exists(log_path):
        return []

    try:
        with open(log_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        entry = json.loads(line)
                        usage_data.append(entry)
                    except json.JSONDecodeError:
                        continue
    except Exception as e:
        print(f"Error reading log file: {e}")
        return []

    return usage_data

def parse_timestamps(usage_data):
    """Parse ISO timestamps to datetime objects"""
    for entry in usage_data:
        try:
            entry['datetime'] = datetime.fromisoformat(entry['timestamp'].replace('Z', '+00:00'))
        except:
            # Fallback for different timestamp formats
            try:
                entry['datetime'] = datetime.strptime(entry['timestamp'], '%Y-%m-%dT%H:%M:%S')
            except:
                entry['datetime'] = datetime.now()

    return sorted(usage_data, key=lambda x: x['datetime'])

def analyze_usage(log_file='~/.claude/skill-usage/usage.jsonl'):
    """Analyze skill usage from log file"""

    print("=" * 80)
    print("SKILL USAGE ANALYSIS")
    print("=" * 80)

    # Load data
    usage_data = load_usage_data(log_file)

    if not usage_data:
        print("\n⚠️  No usage data found yet.")
        print("\nThe tracking system is set up and ready!")
        print("Start using skills with the /skill command and data will be collected automatically.")
        print(f"\nLog file: {os.path.expanduser(log_file)}")
        return

    # Parse timestamps
    usage_data = parse_timestamps(usage_data)

    # Basic stats
    print(f"\n📊 Total skill invocations: {len(usage_data)}")
    print(f"📅 First use: {usage_data[0]['datetime'].strftime('%Y-%m-%d %H:%M')}")
    print(f"📅 Last use: {usage_data[-1]['datetime'].strftime('%Y-%m-%d %H:%M')}")

    # Most used skills
    skill_counts = Counter(entry['skill'] for entry in usage_data)
    print("\n" + "=" * 80)
    print("🏆 TOP 20 MOST USED SKILLS")
    print("=" * 80)
    print(f"{'Skill':<45} {'Uses':>6} {'%':>7}")
    print("-" * 80)

    for skill, count in skill_counts.most_common(20):
        percentage = (count / len(usage_data)) * 100
        bar = '█' * min(int(percentage), 40)
        print(f"{skill:<45} {count:>6} {percentage:>6.1f}% {bar}")

    # Time-based analysis
    now = datetime.now()
    last_7_days = [e for e in usage_data if e['datetime'] > now - timedelta(days=7)]
    last_30_days = [e for e in usage_data if e['datetime'] > now - timedelta(days=30)]

    print("\n" + "=" * 80)
    print("📈 USAGE BY TIME PERIOD")
    print("=" * 80)
    print(f"Last 7 days:  {len(last_7_days):>4} uses")
    print(f"Last 30 days: {len(last_30_days):>4} uses")
    print(f"All time:     {len(usage_data):>4} uses")

    if last_7_days:
        recent_skills = Counter(e['skill'] for e in last_7_days)
        print("\n🔥 Top 5 skills (last 7 days):")
        for skill, count in recent_skills.most_common(5):
            print(f"  {count:>2}× {skill}")

    # Usage patterns - Day of week
    print("\n" + "=" * 80)
    print("📅 USAGE BY DAY OF WEEK")
    print("=" * 80)

    day_counts = defaultdict(int)
    for entry in usage_data:
        day = entry['datetime'].strftime('%A')
        day_counts[day] += 1

    days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    max_count = max(day_counts.values()) if day_counts else 1

    for day in days_order:
        count = day_counts.get(day, 0)
        bar_length = int((count / max_count) * 40) if max_count > 0 else 0
        bar = '█' * bar_length
        print(f"{day:<10} {count:>4} {bar}")

    # Usage patterns - Hour of day
    print("\n" + "=" * 80)
    print("🕐 USAGE BY HOUR OF DAY")
    print("=" * 80)

    hour_counts = defaultdict(int)
    for entry in usage_data:
        hour = entry['datetime'].hour
        hour_counts[hour] += 1

    max_hour_count = max(hour_counts.values()) if hour_counts else 1

    for hour in range(24):
        count = hour_counts.get(hour, 0)
        if count > 0:  # Only show hours with activity
            bar_length = int((count / max_hour_count) * 40) if max_hour_count > 0 else 0
            bar = '█' * bar_length
            print(f"{hour:02d}:00 {count:>4} {bar}")

    # Coverage analysis
    print("\n" + "=" * 80)
    print("📊 SKILL COVERAGE")
    print("=" * 80)

    # Try to load all skills
    skills_file = 'skills-knowledge-graph.json'
    if os.path.exists(skills_file):
        try:
            with open(skills_file, 'r', encoding='utf-8') as f:
                all_skills_data = json.load(f)
                all_skill_ids = {s['id'] for s in all_skills_data['skills']}
                used_skill_ids = {e['skill'] for e in usage_data}
                unused_skills = all_skill_ids - used_skill_ids

                print(f"Total skills:   {len(all_skill_ids):>4}")
                print(f"Used skills:    {len(used_skill_ids):>4} ({len(used_skill_ids)/len(all_skill_ids)*100:>5.1f}%)")
                print(f"Unused skills:  {len(unused_skills):>4} ({len(unused_skills)/len(all_skill_ids)*100:>5.1f}%)")

                if unused_skills and len(unused_skills) <= 30:
                    print(f"\n❌ Unused skills ({len(unused_skills)}):")
                    for skill_id in sorted(list(unused_skills)[:20]):
                        skill = next((s for s in all_skills_data['skills'] if s['id'] == skill_id), None)
                        if skill:
                            print(f"  - {skill['name']}")
                    if len(unused_skills) > 20:
                        print(f"  ... and {len(unused_skills) - 20} more")
        except Exception as e:
            print(f"Could not load skills data: {e}")
    else:
        print("Skills data file not found - skipping coverage analysis")

    # Recommendations
    print("\n" + "=" * 80)
    print("💡 RECOMMENDATIONS")
    print("=" * 80)

    # Skills used only once
    single_use = [skill for skill, count in skill_counts.items() if count == 1]
    if single_use:
        print(f"\n⚠️  {len(single_use)} skills used only once (consider if needed):")
        for skill in sorted(single_use[:10]):
            print(f"  - {skill}")
        if len(single_use) > 10:
            print(f"  ... and {len(single_use) - 10} more")

    # Core skills check
    core_skills = ['brainstorming', 'writing-plans', 'executing-plans',
                   'verification-before-completion', 'code-reviewer', 'systematic-debugging']

    if last_7_days:
        recent_skill_ids = {e['skill'] for e in last_7_days}
        unused_core = [s for s in core_skills if s not in recent_skill_ids]
        if unused_core:
            print(f"\n⚠️  Core skills not used in last 7 days:")
            for skill in unused_core:
                print(f"  - {skill}")

    print("\n" + "=" * 80)
    print("✅ Analysis complete!")
    print("=" * 80)

if __name__ == '__main__':
    import sys
    sys.stdout.reconfigure(encoding='utf-8')
    log_file = sys.argv[1] if len(sys.argv) > 1 else '~/.claude/skill-usage/usage.jsonl'
    analyze_usage(log_file)

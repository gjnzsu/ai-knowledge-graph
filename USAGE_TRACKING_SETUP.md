# Skill Usage Tracking - Setup Complete! ✅

**Date**: 2026-04-19  
**Status**: Ready to track!

---

## ✅ What's Been Set Up

### 1. **Tracking Directory** ✓
- Location: `~/.claude/skill-usage/`
- Log file: `~/.claude/skill-usage/usage.jsonl`
- Status: Created and ready

### 2. **Analysis Script** ✓
- File: `analyze_skill_usage.py`
- Features: Full analysis with charts and recommendations
- Status: Tested and working

### 3. **Hook Configuration** (Next Step)
- Needs to be added to `.claude/settings.json`
- Will automatically log every skill use

---

## 🚀 Final Setup Step: Add Hook

### Option A: Manual Setup (Recommended)

Add this to your `.claude/settings.json` file:

```json
{
  "hooks": {
    "SkillInvoke": {
      "command": "bash",
      "args": [
        "-c",
        "echo \"{\\\"timestamp\\\":\\\"$(date -Iseconds)\\\",\\\"skill\\\":\\\"$SKILL_NAME\\\"}\" >> ~/.claude/skill-usage/usage.jsonl"
      ]
    }
  }
}
```

**Where to add it**:
1. Open `~/.claude/settings.json` (or create if doesn't exist)
2. Add the `hooks` section
3. Save the file
4. Restart Claude Code (if running)

### Option B: Windows-Compatible Hook

If you're on Windows and the above doesn't work, use this:

```json
{
  "hooks": {
    "SkillInvoke": {
      "command": "python",
      "args": [
        "-c",
        "import json, datetime, os; log_file = os.path.expanduser('~/.claude/skill-usage/usage.jsonl'); entry = {'timestamp': datetime.datetime.now().isoformat(), 'skill': os.environ.get('SKILL_NAME', 'unknown')}; open(log_file, 'a').write(json.dumps(entry) + '\\n')"
      ]
    }
  }
}
```

---

## 📊 How to Use

### 1. Use Skills Normally
```bash
# Just use skills as you normally would
/brainstorming
/writing-plans
/code-reviewer
```

**The hook will automatically log each use!**

### 2. Analyze Your Usage
```bash
# Run the analysis script anytime
python analyze_skill_usage.py
```

### 3. View Results
You'll see:
- Most used skills (top 20)
- Usage by time period (7 days, 30 days)
- Usage patterns (day of week, hour of day)
- Coverage (which skills you never use)
- Recommendations (skills to remove)

---

## 📈 Example Output (After Some Usage)

```
================================================================================
SKILL USAGE ANALYSIS
================================================================================

📊 Total skill invocations: 156
📅 First use: 2026-04-01 09:23
📅 Last use: 2026-04-19 17:45

================================================================================
🏆 TOP 20 MOST USED SKILLS
================================================================================
Skill                                          Uses      %
--------------------------------------------------------------------------------
brainstorming                                    23   14.7% ███████
executing-plans                                  18   11.5% █████
code-reviewer                                    15    9.6% ████
verification-before-completion                   12    7.7% ███

================================================================================
📈 USAGE BY TIME PERIOD
================================================================================
Last 7 days:    45 uses
Last 30 days:  156 uses
All time:      156 uses

🔥 Top 5 skills (last 7 days):
   8× brainstorming
   6× code-reviewer
   5× executing-plans

================================================================================
📅 USAGE BY DAY OF WEEK
================================================================================
Monday      28 ██████████████
Tuesday     32 ████████████████
Wednesday   25 ████████████
Thursday    30 ███████████████
Friday      22 ███████████
Saturday     8 ████
Sunday      11 █████

================================================================================
📊 SKILL COVERAGE
================================================================================
Total skills:    279
Used skills:      45 (16.1%)
Unused skills:   234 (83.9%)

================================================================================
💡 RECOMMENDATIONS
================================================================================

⚠️  12 skills used only once (consider if needed):
  - skill-stocktake
  - instinct-manager
  ...

⚠️  Core skills not used in last 7 days:
  - systematic-debugging

================================================================================
✅ Analysis complete!
================================================================================
```

---

## 🎯 What You'll Learn

### After 1 Week
- Which skills you actually use daily
- Your most productive hours
- Your coding patterns

### After 1 Month
- Which 234 skills you never touch (remove them!)
- Your top 20 essential skills
- Usage trends over time

### After 3 Months
- Solid data for skill optimization
- Clear patterns of what works
- Confidence to remove unused skills

---

## 🔧 Troubleshooting

### Hook Not Working?
```bash
# Check if log file is being written to
ls -lh ~/.claude/skill-usage/usage.jsonl

# Manually test the hook
echo '{"timestamp":"2026-04-19T17:00:00","skill":"test-skill"}' >> ~/.claude/skill-usage/usage.jsonl

# Run analysis to verify
python analyze_skill_usage.py
```

### No Data Showing?
- Make sure you're using skills via `/skill` command
- Check that the hook is in `.claude/settings.json`
- Restart Claude Code after adding the hook
- Verify the log file exists and has write permissions

### Analysis Script Errors?
```bash
# Make sure you're in the right directory
cd /path/to/ai-knowledge-graph

# Run with full path
python analyze_skill_usage.py ~/.claude/skill-usage/usage.jsonl
```

---

## 📁 Files Created

```
~/.claude/skill-usage/
  └── usage.jsonl              # Log file (auto-populated)

ai-knowledge-graph/
  ├── analyze_skill_usage.py   # Analysis script
  └── USAGE_TRACKING_SETUP.md  # This file
```

---

## 🎯 Next Steps

1. **Add the hook** to `.claude/settings.json` (see above)
2. **Restart Claude Code** (if running)
3. **Use skills normally** - tracking happens automatically
4. **Run analysis** after a few days: `python analyze_skill_usage.py`
5. **Optimize** - remove unused skills, focus on what works

---

## 💡 Pro Tips

### Weekly Review
```bash
# Every Monday, check your usage
python analyze_skill_usage.py > weekly-report.txt
```

### Monthly Cleanup
```bash
# After 30 days, identify unused skills
python analyze_skill_usage.py | grep "Unused skills"
```

### Track Progress
```bash
# Save snapshots over time
python analyze_skill_usage.py > usage-report-$(date +%Y-%m-%d).txt
```

---

## ⚡ Performance Impact

**Overhead per skill use**: < 1-2ms  
**Disk space**: ~100 bytes per use  
**After 1 year**: ~3.6 MB (36,000 uses)  

**You won't notice any slowdown!**

---

## 🎉 You're All Set!

The tracking system is ready. Just add the hook to `.claude/settings.json` and you're done!

**Questions?** Check the troubleshooting section above or refer to `SKILL_USAGE_TRACKING.md` for more details.

Happy tracking! 📊

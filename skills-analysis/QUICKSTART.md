# Skills Knowledge Graph - Quick Start Guide

## Two Versions Available

### 1. **Standalone Version** (Recommended - No Server Needed!)
**File**: `skills-graph-standalone.html`  
**Size**: 178 KB  
**Data**: Embedded directly in HTML

✅ **Just double-click to open** - works immediately in any browser  
✅ No server required  
✅ No CORS issues  
✅ Works offline  

**How to use**:
```bash
# Windows
start skills-graph-standalone.html

# Mac
open skills-graph-standalone.html

# Linux
xdg-open skills-graph-standalone.html
```

Or simply **double-click the file** in your file explorer!

---

### 2. **Server Version** (Requires HTTP Server)
**File**: `enhanced-skills-graph.html`  
**Size**: 20 KB  
**Data**: Loads from `skills-knowledge-graph.json`

Requires running a local server:
```bash
# Start server
python -m http.server 8000

# Open in browser
http://localhost:8000/enhanced-skills-graph.html
```

---

## Features (Both Versions)

### ✨ Interactive Graph
- **300 skills** displayed as individual nodes
- **446 relationships** visualized with colored lines
- **10 category lanes** organizing skills horizontally
- Color-coded by category

### 🔍 Filtering & Search
- **Dropdown filter**: Select any skill to highlight it and neighbors
- **Category filter**: Show only specific categories
- **Search box**: Real-time search across names and descriptions
- **Smart highlighting**: Selected skill (blue) + neighbors highlighted, others dimmed

### 📋 Card View
Each card shows:
- Skill name and category badge
- Purpose/description
- Number of related skills
- Number of dependencies
- Click to select and sync with graph

### 🎛️ View Modes
- **Graph View**: Interactive network + cards sidebar
- **Cards Only**: Full-width card list

---

## Quick Tips

1. **Select a skill**: Use dropdown or click any node/card
2. **Explore relationships**: Selected skill and its neighbors are highlighted
3. **Filter by category**: See only skills in specific domains
4. **Search**: Type to filter skills in real-time
5. **Toggle views**: Switch between graph and cards-only mode

---

## File Comparison

| Feature | Standalone | Server Version |
|---------|-----------|----------------|
| File size | 178 KB | 20 KB + 206 KB JSON |
| Setup | None | HTTP server |
| CORS issues | None | Possible |
| Offline | ✅ Yes | ✅ Yes (with server) |
| Updates | Rebuild file | Edit JSON |
| Best for | Quick viewing | Development |

---

## Troubleshooting

### Standalone Version
**Problem**: File won't open  
**Solution**: Right-click → Open with → Choose your browser

**Problem**: Blank page  
**Solution**: Check browser console (F12) for errors

### Server Version
**Problem**: CORS error  
**Solution**: Use the standalone version or ensure server is running

**Problem**: Data not loading  
**Solution**: Verify `skills-knowledge-graph.json` is in the same directory

---

## Statistics

- **300 skills** across 10 categories
- **446 relationships** mapped
- **10 categories**: Core, Code Review, Testing, Frameworks, Agents, Product, Docs, Infrastructure, Financial, Domain-specific

---

**Recommended**: Use `skills-graph-standalone.html` for the best experience!

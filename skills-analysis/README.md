# Skills Knowledge Graph - Enhanced Visualization

An interactive visualization of all your Claude Code skills showing relationships, dependencies, and detailed information.

## Features

### 1. **Individual Skill Nodes**
- All 300 skills displayed as individual nodes
- Color-coded by category
- Organized in horizontal lanes by category

### 2. **Relationship Visualization**
- **446 relationships** mapped between skills
- Different line styles for different relationship types:
  - `depends_on` - Red lines (hard dependencies)
  - `invokes` - Orange lines (calls/uses)
  - `related_to` - Blue lines (complementary skills)

### 3. **Interactive Filtering**
- **Dropdown filter**: Select any skill to highlight it and its immediate neighbors
- **Category filter**: Show only skills from specific categories
- **Search box**: Real-time search across skill names and descriptions
- Selected skills are highlighted in blue with thicker borders
- Neighbors are highlighted, unrelated skills are dimmed

### 4. **Card View**
Each skill card shows:
- Skill name and category
- Purpose/description
- Number of related skills
- Number of dependencies
- Click any card to highlight it in the graph

### 5. **Dual View Modes**
- **Graph View** (default): Interactive network visualization with cards sidebar
- **Cards Only**: Full-width card list for detailed browsing

## How to Use

1. **Open the visualization**:
   ```bash
   # Open in your browser
   open skills-analysis/enhanced-skills-graph.html
   # or
   start skills-analysis/enhanced-skills-graph.html
   ```

2. **Explore skills**:
   - Use the dropdown to select a specific skill
   - The graph will highlight the selected skill (blue) and its neighbors
   - Unrelated skills are dimmed for focus

3. **Filter by category**:
   - Select a category from the dropdown
   - Only skills in that category will be shown

4. **Search**:
   - Type in the search box to filter skills by name or description
   - Results update in real-time

5. **Click interactions**:
   - Click any node in the graph to select it
   - Click any card in the sidebar to select it
   - Selected items are synchronized between graph and cards

## File Structure

```
ai-knowledge-graph/
├── skills-knowledge-graph.json          # Complete skill data (300 skills, 446 relationships)
├── skills-analysis/
│   ├── enhanced-skills-graph.html       # Interactive visualization
│   ├── skills-knowledge-graph.json      # Data file (copy for easy access)
│   ├── core-superpowers.md              # Source: Core skills
│   ├── code-review-skills.md            # Source: Code review
│   ├── build-testing-skills.md          # Source: Build & testing
│   ├── framework-language-patterns.md   # Source: Framework patterns
│   ├── agent-orchestration-skills.md    # Source: Agent orchestration
│   ├── product-management-skills.md     # Source: Product management
│   ├── documentation-content-design.md  # Source: Documentation
│   ├── infrastructure-devops-database.md # Source: Infrastructure
│   ├── financial-business-skills.md     # Source: Financial analysis
│   └── domain-specialized-skills.md     # Source: Domain-specific
└── graphify-out/
    ├── graph.html                       # Simple category-level graph
    ├── graph.json                       # Category-level graph data
    └── GRAPH_REPORT.md                  # Analysis report
```

## Categories (10 Total)

1. **Core Superpowers** (14 skills) - Foundation workflows and best practices
2. **Code Review** (11 skills) - Language-specific code reviewers
3. **Build and Testing** (24 skills) - Build resolvers, TDD, verification
4. **Framework and Language Patterns** (34 skills) - Multi-language/framework support
5. **Agent Orchestration** (29 skills) - Multi-agent systems, autonomous loops
6. **Product Management** (38 skills) - Discovery, strategy, design thinking
7. **Documentation and Content** (34 skills) - Documents, presentations, media
8. **Infrastructure and DevOps** (37 skills) - Deployment, databases, architecture
9. **Financial and Business** (31 skills) - Modeling, metrics, investor relations
10. **Domain Specialized** (48 skills) - Healthcare, logistics, supply chain, energy

## Key Statistics

- **300 skills** across 10 categories
- **446 relationships** mapped
- **100% extraction rate** from source markdown files
- **10 source files** analyzed

## Example Use Cases

### Find Related Skills
1. Select "brainstorming" from the dropdown
2. See all related skills highlighted: writing-plans, executing-plans, etc.
3. Click on any neighbor to explore further

### Explore a Domain
1. Select "Healthcare Domain" from category filter
2. Browse all healthcare-related skills
3. See dependencies and relationships

### Discover Dependencies
1. Search for "test-driven-development"
2. View the card to see related testing skills
3. Click to see the graph connections

## Technical Details

- Built with D3.js v7 for graph visualization
- Responsive design with dark theme
- No server required - runs entirely in browser
- Data loaded from JSON file
- Smooth animations and transitions

## Troubleshooting

**Graph not loading?**
- Ensure `skills-knowledge-graph.json` is in the parent directory
- Check browser console for errors
- Try opening in a different browser (Chrome/Firefox recommended)

**Skills not filtering?**
- Clear the search box
- Reset category filter to "All Categories"
- Refresh the page

## Future Enhancements

Potential additions:
- Export filtered view as image
- Skill comparison mode
- Dependency path finder
- Cluster analysis view
- Timeline view (when skills were added)

---

**Generated**: 2026-04-19  
**Total Skills**: 300  
**Total Relationships**: 446  
**Categories**: 10

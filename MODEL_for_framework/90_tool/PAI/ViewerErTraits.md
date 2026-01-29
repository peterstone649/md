# ViewerErTraits

**Purpose**: A viewer tool to display and present the Traits markdown content for agent composition.

**Location**: `E:\2025_11\md\MODEL_for_framework\90_tool\PAI\ViewerErTraits.md`

## Package Information
- **Package**: `online.wikx.n10.util.er`
- **Class Name**: `ViewerErTraits`
- **Type**: Markdown Viewer

## Functionality

### 1. Markdown Content Display
The ViewerErTraits tool provides functionality to display the complete ListTraits.md content in a structured format.

### 2. Content Presentation
- Displays all available traits organized by categories
- Shows expertise areas, personality dimensions, and approach styles
- Includes example compositions and usage scenarios
- Provides voice mapping information for trait combinations

### 3. Viewer Capabilities
- **Complete Content Display**: Shows the entire ListTraits.md content
- **Structured Organization**: Maintains the original markdown structure and formatting
- **Category Separation**: Clearly separates expertise, personality, and approach traits
- **Example Showcase**: Displays predefined trait combinations and use cases

## Viewer Content

### Complete ListTraits.md Content

```markdown
# ListTraits Workflow

**Shows all available traits that can be composed into custom agents.**

## When to Use

User says:
- "What agent personalities can you create?"
- "Show me available traits"
- "List agent types"
- "What expertise areas do you have?"

## The Workflow

### Step 1: Run AgentFactory with --list Flag

```bash
bun run ~/.claude/skills/Agents/Tools/AgentFactory.ts --list
```

### Step 2: Present Results to User

The tool outputs:

```
AVAILABLE TRAITS

EXPERTISE (domain knowledge):
  security        - Security Expert
  legal           - Legal Analyst
  finance         - Financial Analyst
  medical         - Medical/Health Expert
  technical       - Technical Specialist
  research        - Research Specialist
  creative        - Creative Specialist
  business        - Business Strategist
  data            - Data Analyst
  communications  - Communications Expert

PERSONALITY (behavior style):
  skeptical       - Skeptical
  enthusiastic    - Enthusiastic
  cautious        - Cautious
  bold            - Bold
  analytical      - Analytical
  creative        - Creative
  empathetic      - Empathetic
  contrarian      - Contrarian
  pragmatic       - Pragmatic
  meticulous      - Meticulous

APPROACH (work style):
  thorough        - Thorough
  rapid           - Rapid
  systematic      - Systematic
  exploratory     - Exploratory
  comparative     - Comparative
  synthesizing    - Synthesizing
  adversarial     - Adversarial
  consultative    - Consultative

EXAMPLE COMPOSITIONS:
  security_audit       - Security architecture review
                         traits: security, skeptical, thorough, adversarial
  contract_review      - Legal contract analysis
                         traits: legal, cautious, meticulous, systematic
  market_analysis      - Competitive market research
                         traits: business, analytical, comparative, thorough
  code_review          - Technical code review
                         traits: technical, meticulous, systematic
  creative_brief       - Creative content development
                         traits: creative, enthusiastic, exploratory
  red_team             - Adversarial idea testing
                         traits: contrarian, skeptical, adversarial, bold
  user_research        - User experience research
                         traits: research, empathetic, synthesizing
  quick_assessment     - Rapid evaluation needed
                         traits: analytical, pragmatic, rapid
```

### Step 3: Explain Composition System

Add context for user:

```
You can combine these traits to create custom agents:

EXPERTISE + PERSONALITY + APPROACH = Custom Agent

Examples:
- "Create a security expert who's skeptical and thorough"
  → security + skeptical + thorough

- "I need someone with legal knowledge who's really careful"
  → legal + cautious + meticulous

- "Get me a creative thinker who works fast"
  → creative + enthusiastic + rapid

Just describe what you need naturally, and I'll compose the right agent.
```

## Enhanced Presentation (Optional)

If user wants more detail, also explain voice assignment:

```
Each trait combination maps to a unique voice:

ENERGETIC VOICES (enthusiastic, creative, bold):
- Jeremy (excited Irish-American male)
- Fin (energetic Irish storyteller)
- Freya (vibrant dynamic female)
- Dave (youthful British energy)

INTELLECTUAL VOICES (analytical, skeptical, research):
- Default (BBC anchor authority)
- George (academic warm raspy)
- Charlotte (sophisticated Swedish-British)
- Antoni (professorial articulate)

AUTHORITATIVE VOICES (bold, business, cautious):
- Domi (assertive CEO female)
- Bill (documentary trustworthy male)
- Alice (confident news anchor female)
- Joseph (formal British authority)

WARM VOICES (empathetic, consultative):
- Matilda (friendly American storyteller)
- Thomas (calm gentle guide)
- Rachel (calm supportive)

EDGY VOICES (adversarial, contrarian, security):
- Clyde (gravelly war veteran intensity)
- Callum (hoarse hacker character)
- Sam (raspy gritty authentic)
```

## Example Interaction

**User:** "What kinds of agents can you create?"

**System:**
```
I can compose agents from 28 traits across three categories:

EXPERTISE (what they know):
security, legal, finance, medical, technical, research, creative,
business, data, communications

PERSONALITY (how they think):
skeptical, enthusiastic, cautious, bold, analytical, creative,
empathetic, contrarian, pragmatic, meticulous

APPROACH (how they work):
thorough, rapid, systematic, exploratory, comparative, synthesizing,
adversarial, consultative

Just tell me what you need:
- "I need a legal expert who's really thorough"
- "Create a skeptical security analyst"
- "Get me someone creative and fast"

I'll compose the right agent with a matching voice.
```

## Quick Reference Card (Optional)

For frequent use, provide a condensed version:

```
QUICK TRAIT REFERENCE

Expertise:     security | legal | finance | medical | technical |
               research | creative | business | data | communications

Personality:   skeptical | enthusiastic | cautious | bold | analytical |
               creative | empathetic | contrarian | pragmatic | meticulous

Approach:      thorough | rapid | systematic | exploratory | comparative |
               synthesizing | adversarial | consultative

Popular Combos:
- Security audit:     security + skeptical + adversarial
- Contract review:    legal + cautious + meticulous
- Creative brief:     creative + enthusiastic + exploratory
- Code review:        technical + meticulous + systematic
- Red team:           contrarian + skeptical + bold
```

## Related Workflows

- **CreateCustomAgent** - Actually create agents with these traits
- **SpawnParallelAgents** - Launch generic agents (no trait customization)

## References

- Full trait definitions: `~/.claude/skills/Agents/Data/Traits.yaml`
- Voice mappings: Lines 349-794 in Traits.yaml
- AgentFactory tool: `~/.claude/skills/Agents/Tools/AgentFactory.ts`
```

## Usage Examples

### Basic Viewer Usage
```markdown
# To display all available traits:

ViewerErTraits.showAllTraits()

# To display traits by category:

ViewerErTraits.showExpertiseTraits()
ViewerErTraits.showPersonalityTraits()
ViewerErTraits.showApproachTraits()

# To display example compositions:

ViewerErTraits.showExampleCompositions()
```

### Advanced Viewer Usage
```markdown
# To display the complete workflow:

ViewerErTraits.showCompleteWorkflow()

# To display voice mapping information:

ViewerErTraits.showVoiceMappings()

# To display quick reference:

ViewerErTraits.showQuickReference()
```

## Implementation Details

### Viewer Methods
- `showAllTraits()`: Displays all available traits organized by categories
- `showExpertiseTraits()`: Shows only expertise traits
- `showPersonalityTraits()`: Shows only personality traits
- `showApproachTraits()`: Shows only approach traits
- `showExampleCompositions()`: Displays predefined trait combinations
- `showCompleteWorkflow()`: Shows the entire ListTraits workflow
- `showVoiceMappings()`: Displays voice assignment information
- `showQuickReference()`: Shows condensed trait reference

### Data Structure
The viewer maintains the original markdown structure and formatting from ListTraits.md, ensuring consistent presentation.

## Integration

The ViewerErTraits tool can be integrated with agent composition systems to:

1. **Trait Display**: Show available traits to users for agent creation
2. **Education**: Help users understand the trait composition system
3. **Reference**: Provide quick access to trait information
4. **Workflow Integration**: Display trait information during agent creation workflows

## Error Handling

- Validates markdown content structure
- Provides fallback display options if content is missing
- Maintains consistent formatting across different display methods

## Related Tools

- **ReaderForTrait**: For parsing and analyzing Traits.yaml
- **AgentFactory**: For creating agents with specific traits
- **ListTraits**: The original workflow this viewer displays

## Technical Notes

- **File Location**: `E:\2025_11\md\MODEL_for_framework\90_tool\PAI\ViewerErTraits.md`
- **Source Content**: Based on `E:\2025_11\PAI\Packs\pai-agents-skill\src\skills\Agents\Workflows\ListTraits.md`
- **Package**: `online.wikx.n10.util.er`
- **Class Name**: `ViewerErTraits`
- **Format**: Markdown viewer for trait display
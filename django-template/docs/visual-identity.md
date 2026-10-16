# Django Enterprise
## Premium Minimal — Visual Identity & Design System

**Document type:** Visual Identity Specification  
**Version:** 1.0  
**Status:** Design Foundation  
**Scope:** Generic, reusable visual identity for Django applications  
**Design direction:** Premium Minimal × Enterprise UI

---

# 1. Design Vision

## 1.1. Overview

Django Enterprise is a reusable visual identity for Django-based applications, designed to combine the reliability of enterprise software with the refinement of premium minimalist interfaces.

The visual language emphasizes clarity, precision, consistency, and understated sophistication. It avoids unnecessary decoration, excessive color usage, and the visual complexity commonly associated with generic administrative dashboards.

The result should feel like a carefully designed professional software product rather than a prebuilt template.

The identity must remain independent of any particular company, business domain, or application. It should work equally well for internal management systems, audit platforms, financial applications, operational dashboards, SaaS products, and developer-oriented tools.

## 1.2. Core Design Principle

> Sophistication through precision, not decoration.

Every visual element must serve a purpose. Typography establishes hierarchy, spacing improves comprehension, cards organize information, and color communicates meaning.

The interface should feel premium because of the quality of its proportions, alignment, contrast, and consistency—not because of gradients, ornamental effects, or excessive animation.

## 1.3. Design Pillars

### Functional Minimalism
- Remove unnecessary visual elements.
- Prioritize content and task completion.
- Use whitespace as an intentional structural element.
- Keep interfaces visually calm, even when displaying complex information.

### Enterprise Reliability
- Use predictable layouts and familiar interaction patterns.
- Maintain consistent behavior across pages and modules.
- Present operational information clearly.
- Distinguish primary actions, secondary actions, and destructive actions.

### Premium Refinement
- Use restrained typography and carefully controlled proportions.
- Prefer subtle borders over heavy shadows.
- Apply a limited, cohesive color palette.
- Give cards and data visualizations a deliberate visual hierarchy.

### Systematic Consistency
- Define reusable design tokens.
- Standardize components, states, spacing, and typography.
- Support light and dark themes.
- Allow individual applications to customize their identity without abandoning the shared design language.

---

# 2. Brand Personality

The design system should communicate the following characteristics:

| Attribute | Visual Interpretation |
|---|---|
| Professional | Structured layouts and disciplined typography |
| Reliable | Consistent interactions and clear status indicators |
| Refined | Restrained colors, fine borders, and balanced proportions |
| Modern | Clean interfaces and responsive layouts |
| Technical | Precise data presentation and optional monospace typography |
| Neutral | No dependence on a specific company or industry |
| Approachable | Clear labels, understandable feedback, and accessible controls |

## 2.1. What the Identity Is Not

The design must not resemble:

- A heavily decorated corporate dashboard.
- A generic admin template filled with colorful cards.
- A neon-themed developer interface.
- A skeuomorphic interface with simulated physical materials.
- A landing page dominated by gradients and oversized illustrations.
- A direct reproduction of the default Django Admin interface.

The identity should feel intentionally designed, not visually overengineered.

---

# 3. Color System

The color system retains the original Django Enterprise palette while applying the restraint of the Premium Minimal direction.

The original navy and steel blue remain the institutional colors. Cool neutrals establish the primary surfaces, while semantic colors are reserved for meaningful feedback.

## 3.1. Primary Palette

### Enterprise Navy

**HEX:** `#26374A`

The primary institutional color.

Usage:
- Primary navigation surfaces when a dark sidebar is desired.
- Selected navigation elements on dark surfaces.
- Strong headings in light interfaces.
- Important structural elements.
- Brand marks and optional application symbols.

Enterprise Navy should establish visual authority without dominating every screen.

### Steel Blue

**HEX:** `#526D8A`

The primary interactive color.

Usage:
- Primary buttons.
- Links and interactive text.
- Selected controls.
- Focus indicators, where contrast permits.
- Active navigation indicators.
- Chart emphasis and selected data series.

Steel Blue should be used selectively. Its purpose is to identify meaningful interactions, not to color every component.

### Cool Mist

**HEX:** `#E9EEF3`

The primary cool secondary surface color.

Usage:
- Secondary content backgrounds.
- Selected navigation backgrounds.
- Subtle highlighted sections.
- Secondary information panels.
- Neutral selected states.

Cool Mist provides separation without introducing strong visual contrast.

### Pure Surface

**HEX:** `#FFFFFF`

The primary content surface.

Usage:
- Cards.
- Forms.
- Tables.
- Dialogs.
- Dropdown menus.
- Content panels.

White should remain the dominant surface color in the default light theme.

## 3.2. Neutral Palette

| Token | HEX | Purpose |
|---|---|---|
| `color-neutral-950` | `#202B38` | Primary text |
| `color-neutral-800` | `#354353` | Secondary headings and strong UI elements |
| `color-neutral-600` | `#526174` | Secondary text |
| `color-neutral-500` | `#747B82` | Muted text and supporting information |
| `color-neutral-300` | `#D9E0E7` | Borders and dividers |
| `color-neutral-100` | `#F4F6F8` | Main light-theme canvas |
| `color-neutral-50` | `#FFFFFF` | Primary content surfaces |

The neutral palette must provide most of the interface's visual structure. Accent colors should remain secondary to content and layout.

## 3.3. Semantic Colors

Semantic colors communicate status and must retain consistent meanings across all applications.

| Semantic role | Foreground | Background | Intended use |
|---|---|---|---|
| Success | `#287D58` | `#E5F4EC` | Completed operations, approved items, successful actions |
| Warning | `#946719` | `#FFF3D8` | Pending tasks, attention required, non-critical warnings |
| Danger | `#B84242` | `#FBE9E9` | Errors, failed operations, destructive actions |
| Information | `#3C6D9A` | `#E8F0FA` | Contextual guidance and informational messages |

Semantic colors must not replace the institutional palette.

For example, green should not become the default primary button color simply because it is visually attractive. It should remain associated with success and positive states.

Color must never be the sole means of communicating status. Pair it with labels, icons, or descriptive text.

## 3.4. Color Distribution

The recommended visual balance is:

- **70–80%:** neutral backgrounds and content surfaces.
- **15–25%:** typography, borders, and structural elements.
- **A small remainder:** interactive accents and semantic feedback.

These proportions are directional rather than strict numerical requirements.

The interface should feel neutral at first glance, with accent colors becoming noticeable only where they communicate useful information.

---

# 4. Light Theme

## 4.1. Visual Direction

The light theme is the primary reference for the design system.

It uses cool gray backgrounds, white content surfaces, restrained borders, and dark blue-gray typography.

The interface should feel open and organized without becoming excessively bright or sterile.

## 4.2. Surface Hierarchy

| Surface | Color | Purpose |
|---|---|---|
| Application canvas | `#F4F6F8` | Main page background |
| Primary surface | `#FFFFFF` | Cards and content panels |
| Secondary surface | `#E9EEF3` | Highlighted sections and selected elements |
| Border | `#D9E0E7` | Component boundaries |
| Primary text | `#202B38` | Main content |
| Secondary text | `#526174` | Supporting content |
| Muted text | `#747B82` | Metadata and secondary labels |

The distinction between the page canvas and the card surface should be visible but subtle.

Avoid strong shadows to create separation. Prefer background contrast and fine borders.

## 4.3. Recommended Appearance

- White cards placed on a light neutral canvas.
- Thin borders with low visual prominence.
- Dark text with strong readability.
- Steel Blue reserved for interactions.
- Consistent spacing between sections.
- Minimal use of decorative icons.
- No unnecessary gradients.

---

# 5. Dark Theme

## 5.1. Visual Direction

The dark theme must preserve the same hierarchy and personality as the light theme.

It should not be a simple color inversion. Instead, it should use a dedicated set of dark surfaces, borders, and text colors.

The result should feel sophisticated, legible, and calm.

## 5.2. Dark Palette

| Token | HEX | Purpose |
|---|---|---|
| `color-dark-canvas` | `#171F29` | Main application background |
| `color-dark-surface` | `#202B38` | Cards and primary surfaces |
| `color-dark-elevated` | `#26374A` | Dialogs and elevated surfaces |
| `color-dark-border` | `#354353` | Dividers and component boundaries |
| `color-dark-text` | `#E5EBF2` | Primary text |
| `color-dark-muted` | `#B3C0CE` | Secondary text |
| `color-dark-accent` | `#91A9C3` | Interactive accents and selected elements |

The lighter Steel Blue variation is intended for dark surfaces where the original Steel Blue would not provide sufficient contrast.

Semantic colors should also receive dark-theme variants rather than retaining their light backgrounds unchanged.

## 5.3. Dark Theme Rules

- Avoid pure black as the dominant background.
- Preserve separation between cards and the application canvas.
- Use lighter text for primary information and muted text for metadata.
- Keep borders subtle but visible.
- Preserve the same component geometry as the light theme.
- Use accent colors selectively.
- Ensure interactive states remain distinguishable.

---

# 6. Typography

Typography is one of the primary tools for establishing the Premium Minimal identity.

The system should use a restrained typographic hierarchy, with consistent sizes, weights, and line heights.

## 6.1. Primary Typeface: Inter

Inter is the default typeface for interface elements and application content.

Usage:
- Navigation.
- Body text.
- Forms.
- Tables.
- Buttons.
- Labels.
- Notifications.
- Metadata.

Recommended weights:

| Weight | Usage |
|---|---|
| Regular 400 | Body text and descriptions |
| Medium 500 | Labels and secondary emphasis |
| Semibold 600 | Section headings and important controls |
| Bold 700 | Reserved for strong emphasis |

Avoid using bold typography everywhere. Weight should communicate hierarchy.

## 6.2. Secondary Typeface: Manrope

Manrope is an optional typeface for selected headings and prominent metrics.

Usage:
- Main page headings.
- Dashboard metrics.
- Empty-state headings.
- Product-specific presentation pages.

Manrope should not replace Inter throughout the interface. Its purpose is to introduce subtle personality.

For applications requiring a particularly restrained appearance, Inter alone is an entirely valid choice.

## 6.3. Technical Typeface: JetBrains Mono

JetBrains Mono is reserved for technical information.

Usage:
- Identifiers.
- Version numbers.
- Logs.
- Code snippets.
- Request IDs.
- Timestamps when fixed-width alignment is useful.
- Technical metadata.

Avoid using monospace typography for ordinary prose, navigation, or general form labels.

## 6.4. Type Scale

| Token | Size | Line height | Typical usage |
|---|---:|---:|---|
| `text-xs` | 12px | 16px | Metadata and compact annotations |
| `text-sm` | 14px | 20px | Labels and secondary text |
| `text-base` | 16px | 24px | Standard body text |
| `text-lg` | 18px | 28px | Introductory text and emphasis |
| `text-xl` | 20px | 28px | Card headings |
| `text-2xl` | 24px | 32px | Page section headings |
| `text-3xl` | 30px | 36px | Main page headings |
| `text-4xl` | 36px | 44px | Optional presentation headings |

Dense operational interfaces should prioritize the smaller sizes, while overview pages can use larger headings.

Do not make every section heading oversized. Premium Minimal relies on proportion and hierarchy rather than scale alone.

---

# 7. Layout and Spacing

## 7.1. General Principle

Whitespace is a structural element.

Spacing should separate logical groups, establish hierarchy, and make dense information easier to scan.

The design should not maximize whitespace at the expense of operational efficiency. Tables, logs, and administrative screens still need to display meaningful amounts of information.

## 7.2. Spacing Scale

Use a consistent spacing scale based on multiples of four pixels.

| Token | Value | Usage |
|---|---:|---|
| `space-1` | 4px | Tight icon and label spacing |
| `space-2` | 8px | Compact component spacing |
| `space-3` | 12px | Related content groups |
| `space-4` | 16px | Standard component spacing |
| `space-5` | 20px | Card internals |
| `space-6` | 24px | Section spacing |
| `space-8` | 32px | Major content groups |
| `space-10` | 40px | Large section separation |
| `space-12` | 48px | Major layout transitions |
| `space-16` | 64px | Optional presentation-page spacing |

## 7.3. Page Layout

Recommended structure:

1. Application navigation.
2. Page header.
3. Primary actions.
4. Main content or overview cards.
5. Supporting sections.
6. Optional secondary information.

Page headers should be compact and purposeful.

They typically contain:
- A clear page title.
- An optional short description.
- Breadcrumbs when navigation depth warrants them.
- A primary action, if relevant.
- Optional filters or contextual controls.

Avoid adding decorative subtitles or breadcrumbs that do not help users understand their location.

## 7.4. Responsive Behavior

The layout must adapt to different screen sizes.

- Desktop: use the full navigation and multi-column content layouts where appropriate.
- Tablet: reduce columns and preserve readable card widths.
- Mobile: prioritize essential information, stack content, and simplify navigation.
- Tables: use responsive column strategies or horizontal scrolling when necessary.
- Forms: use a single-column layout on narrow screens.

Responsive behavior must preserve hierarchy and usability rather than simply shrinking desktop layouts.

---

# 8. Card Design System

Cards are a central part of the visual language.

They must preserve the detailed, informative structure of Django Enterprise while adopting the restraint of Premium Minimal.

A card should be treated as a meaningful content container, not a decorative rectangle.

## 8.1. Card Principles

- Use a white surface in light mode.
- Use a dedicated elevated surface in dark mode.
- Prefer thin borders to strong shadows.
- Maintain consistent internal padding.
- Establish a clear hierarchy between headings, content, and actions.
- Avoid unnecessary nested cards.
- Use color only when it communicates state or importance.

## 8.2. Card Geometry

| Property | Default | Notes |
|---|---|---|
| Background | `#FFFFFF` | Light theme |
| Border | `1px solid #D9E0E7` | Subtle separation |
| Border radius | 10px | Standard content cards |
| Internal padding | 20–24px | Based on content density |
| Shadow | None | Default |
| Hover transition | 150–200ms | Interactive cards only |
| Header divider | Optional | Use when it improves separation |

Cards should not rely on large shadows or exaggerated corner radii.

A card should feel like part of the page structure rather than a floating object.

## 8.3. Standard Card Anatomy

A standard card may contain:

1. Header.
2. Title and optional description.
3. Optional header actions.
4. Main content.
5. Optional footer or secondary actions.

Not every card requires all five parts.

Use the simplest structure that clearly communicates the information.

## 8.4. Metric Cards

Metric cards present important numerical information.

Recommended structure:

- Small, descriptive label.
- Prominent numerical value.
- Optional unit or contextual detail.
- Optional comparison with a previous period.
- Optional compact visualization.
- Optional semantic status.

Example:

**Total Requests**

`12,840`

`+8.2% compared with the previous period`

Design rules:

- Keep the label visually secondary.
- Give the main value the strongest typographic emphasis.
- Use semantic colors only for meaningful comparisons.
- Avoid assigning a different accent color to every card.
- Use charts only when they add context.

Metric cards should work equally well with and without a trend indicator.

## 8.5. Information Cards

Information cards organize related content without requiring a numerical KPI.

Recommended elements:

- Heading.
- Optional description.
- Supporting information.
- Optional icon.
- Optional action.

Use these cards for system summaries, recent activity, configuration details, and contextual information.

Do not turn every paragraph or small section into a separate card. Related content should remain grouped where appropriate.

## 8.6. Status Cards

Status cards communicate the state of a process, system, or resource.

Examples:
- Operational.
- Pending.
- Failed.
- Requires attention.
- Completed.

Design rules:

- Use a neutral surface by default.
- Apply semantic color to the status label, icon, or a small indicator.
- Keep the status text explicit.
- Reserve full background coloring for situations where stronger emphasis is genuinely necessary.

A failed process should be immediately identifiable without making the entire dashboard visually aggressive.

## 8.7. Chart Cards

Chart cards combine a visualization with explanatory context.

Recommended structure:

- Chart title.
- Optional subtitle or time range.
- Optional filters.
- Main visualization.
- Optional legend or summary.

Design rules:

- Use a restrained chart palette.
- Maintain adequate contrast between series.
- Avoid decorative gradients.
- Minimize unnecessary gridlines.
- Label axes and values clearly.
- Use tooltips where detailed values are needed.
- Do not communicate series identity through color alone when other distinctions are necessary.

Charts should support decisions rather than merely make the dashboard look sophisticated.

## 8.8. Table Cards

Table cards provide a structured container for operational data.

Recommended structure:

- Title and optional record count.
- Search or filtering controls, when needed.
- Data table.
- Pagination or result summary.
- Optional bulk actions.

Design rules:

- Use subtle horizontal dividers.
- Keep row heights consistent.
- Align numerical values appropriately.
- Use clear column labels.
- Keep row actions visually secondary.
- Avoid excessive borders around every individual cell.

For dense datasets, prioritize readability and scanning efficiency over excessive spacing.

## 8.9. Interactive Cards

Interactive cards are appropriate when the entire card leads to a detail page or represents a selectable item.

Requirements:

- Clearly indicate interactivity.
- Provide visible keyboard focus.
- Use subtle hover feedback.
- Preserve text readability.
- Avoid large movement or dramatic shadows.

Static cards should not look clickable.

## 8.10. Empty-State Cards

Empty states should provide useful guidance without introducing unnecessary decoration.

Recommended structure:

- Optional small icon.
- Clear heading.
- Short explanation.
- Optional primary action.

Example:

**No records found**

There are no records matching the current filters.

`Clear filters`

Avoid oversized illustrations, excessive color, or lengthy explanations.

---

# 9. Buttons and Actions

## 9.1. Primary Button

The primary button represents the main action in a context.

Recommended appearance:
- Steel Blue background.
- White text.
- Moderate corner radius.
- Medium-weight typography.
- Clear hover, focus, active, and disabled states.

Use one visually dominant primary action per logical section whenever practical.

## 9.2. Secondary Button

Secondary actions should use neutral surfaces or outlined treatments.

They must remain visually distinct from the primary action without competing with it.

## 9.3. Tertiary and Ghost Actions

Use text-based or ghost buttons for low-emphasis actions, especially in card headers, toolbars, and tables.

Avoid making every action a filled button.

## 9.4. Destructive Actions

Destructive actions must be identifiable through semantic styling and clear labels.

Examples:
- Delete.
- Revoke access.
- Remove configuration.

For irreversible operations, use a confirmation step when appropriate.

## 9.5. Button States

All interactive buttons must define:
- Default.
- Hover.
- Focus-visible.
- Active.
- Disabled.
- Loading, when applicable.

Transitions should be subtle and must not delay feedback.

---

# 10. Forms and Inputs

Forms should prioritize clarity, predictable behavior, and accessibility.

## 10.1. Input Appearance

- White surface in light mode.
- Subtle neutral border.
- Consistent height and internal padding.
- Clear labels above the field.
- Consistent focus treatment.
- Appropriate spacing between fields.

A default input height of approximately 40–44px is recommended for standard forms.

## 10.2. Labels and Supporting Text

Labels should remain visible when a field contains a value.

Placeholder text must not replace the label.

Supporting text may explain formatting requirements, constraints, or the purpose of a field.

## 10.3. Validation States

### Default
Neutral border and normal text.

### Focused
Visible Steel Blue focus indicator.

### Error
Semantic danger color accompanied by a clear explanation.

### Success
Success styling only when a successful state is meaningful.

Validation should explain how to correct a problem whenever possible.

## 10.4. Form Layout

- Use a single column for most forms.
- Use multiple columns only when fields are logically related and the screen provides sufficient width.
- Group related fields into sections.
- Keep section headings concise.
- Avoid placing every field inside its own card.
- Separate primary submission actions from secondary actions.

---

# 11. Tables and Data Presentation

Tables are essential to enterprise applications and must balance density with clarity.

## 11.1. Table Styling

- White background in light mode.
- Subtle horizontal dividers.
- Restrained column headers.
- Consistent row heights.
- Clear hover states.
- Minimal use of background fills.
- Consistent alignment for similar data types.

## 11.2. Data Hierarchy

Use typography and alignment to distinguish:
- Primary identifiers.
- Descriptive text.
- Numerical values.
- Metadata.
- Status labels.
- Row actions.

Do not use bold text for every important value. Establish a deliberate hierarchy.

## 11.3. Status Badges

Badges should be compact, readable, and semantically meaningful.

Recommended characteristics:
- Small text.
- Moderate horizontal padding.
- Rounded corners.
- Restrained background colors.
- Clear labels.

Badges should not be used as decorative labels for ordinary metadata.

## 11.4. Table Actions

Keep common actions discoverable and secondary to the data.

Avoid displaying numerous prominent buttons in every row. Group less frequent actions into a contextual menu when appropriate.

---

# 12. Navigation and Application Shell

## 12.1. Sidebar

The navigation system should feel stable and understated.

Recommended characteristics:
- Compact iconography.
- Clear labels.
- Consistent item spacing.
- Logical grouping.
- Minimal separators.
- A restrained active state.

Two variants are supported:

**Light sidebar:** White background with dark typography and a subtle selected state.

**Dark sidebar:** Enterprise Navy background with light text and carefully controlled contrast.

The dark variant should not force the rest of the application into dark mode.

## 12.2. Top Navigation

A top bar may contain:
- Application identity.
- Global search, if needed.
- Notifications.
- User menu.
- Theme selector.

Avoid adding every possible control by default.

## 12.3. Page Headers

Page headers should establish context and expose the most relevant action.

Recommended order:
1. Breadcrumbs, when useful.
2. Page title.
3. Optional description.
4. Primary action.
5. Optional filters or secondary controls.

Do not make every page header a large hero section.

---

# 13. Icons and Graphic Elements

Use a consistent outline icon family.

Icons should:
- Have consistent stroke weight.
- Use predictable dimensions.
- Align properly with text.
- Support recognizable actions.
- Avoid unnecessary decoration.

Recommended standard sizes:
- 16px for compact controls.
- 20px for standard interface icons.
- 24px for prominent navigation or section icons.

Use icons alongside labels whenever the meaning of an action may be ambiguous.

Decorative illustrations should be rare and reserved for situations where they genuinely improve comprehension or the product's presentation.

---

# 14. Borders, Shadows, and Elevation

## 14.1. Borders

Borders are the primary tool for separating content surfaces.

Use subtle neutral borders for cards, inputs, menus, and panels.

Avoid strong outlines around every nested element.

## 14.2. Shadows

The default card shadow should be none.

Shadows may be introduced sparingly for:
- Popovers.
- Dropdown menus.
- Modal dialogs.
- Floating panels.
- Specific interactive overlays.

Use shadows to communicate elevation, not to decorate static content.

## 14.3. Elevation Hierarchy

The visual hierarchy should primarily rely on:
1. Surface color.
2. Spacing.
3. Borders.
4. Typography.
5. Shadows, only when necessary.

This keeps the interface lightweight while preserving clear grouping.

---

# 15. Motion and Interaction

Motion should be functional and subtle.

## 15.1. Recommended Timing

| Interaction | Duration |
|---|---:|
| Hover and focus transitions | 150ms |
| Button state transitions | 150–200ms |
| Dropdown appearance | 150–200ms |
| Modal appearance | 180–220ms |
| Larger layout transitions | 200–250ms |

These values are starting points, not rigid requirements.

## 15.2. Motion Principles

- Use opacity and small color changes for most transitions.
- Avoid exaggerated scaling.
- Avoid unnecessary parallax.
- Do not animate static cards continuously.
- Keep interaction feedback immediate.
- Respect reduced-motion preferences.

Animations should help users understand state changes, not attract attention to the interface itself.

---

# 16. Accessibility

Accessibility is a core requirement rather than an optional enhancement.

The design system should target WCAG 2.2 Level AA where applicable.

Requirements include:
- Adequate text contrast.
- Visible keyboard focus.
- Logical keyboard navigation.
- Semantic headings.
- Accessible labels for form controls.
- Clear validation messages.
- Meaningful names for icon-only buttons.
- Status information that does not depend on color alone.
- Responsive layouts that support zoom and narrow screens.
- Respect for reduced-motion preferences.

Aim for a contrast ratio of at least 4.5:1 for normal text and 3:1 for large text, subject to applicable WCAG exceptions.

Do not assume that every palette combination is accessible simply because it follows the visual identity. Validate actual foreground and background combinations, especially for muted text, buttons, badges, and focus indicators.

---

# 17. Design Tokens and Implementation Principles

The identity should be implemented through centralized design tokens rather than scattered hardcoded values.

The following CSS illustrates the intended approach.

```css
:root {
  /* Brand */
  --color-brand-primary: #26374A;
  --color-brand-accent: #526D8A;
  --color-brand-subtle: #E9EEF3;

  /* Surfaces */
  --color-canvas: #F4F6F8;
  --color-surface: #FFFFFF;
  --color-surface-secondary: #E9EEF3;

  /* Text */
  --color-text-primary: #202B38;
  --color-text-secondary: #526174;
  --color-text-muted: #747B82;

  /* Borders */
  --color-border: #D9E0E7;

  /* Typography */
  --font-sans: "Inter", sans-serif;
  --font-display: "Manrope", sans-serif;
  --font-mono: "JetBrains Mono", monospace;

  /* Geometry */
  --radius-sm: 6px;
  --radius-md: 8px;
  --radius-card: 10px;
  --radius-lg: 12px;

  /* Spacing */
  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-5: 20px;
  --space-6: 24px;
  --space-8: 32px;

  /* Effects */
  --shadow-card: none;
  --transition-fast: 150ms ease;
  --transition-normal: 200ms ease;
}
```

A dark theme should override semantic tokens such as canvas, surface, text, and border colors while retaining the same component structure.

Avoid duplicating component styles for every project. Customization should occur through tokens and clearly defined variants.

## 17.1. Component Variants

Components should expose a limited set of intentional variants.

Examples:
- Primary, secondary, and ghost buttons.
- Standard and compact cards.
- Neutral and semantic badges.
- Default, focused, error, and disabled inputs.
- Light and dark navigation shells.

Avoid creating multiple nearly identical variants without a clear functional distinction.

---

# 18. Application-Specific Customization

Django Enterprise is a shared visual foundation, not a fixed product identity.

Individual projects may customize selected elements without changing the core design language.

## 18.1. Fixed Elements

The following should remain consistent:
- Typography.
- Spacing scale.
- Card geometry.
- Button behavior.
- Form styling.
- Table patterns.
- Navigation conventions.
- Semantic colors.
- Accessibility requirements.
- Light and dark theme behavior.

## 18.2. Configurable Elements

The following may vary by application:
- Application name.
- Logo or symbol.
- Accent color, within accessibility constraints.
- Domain-specific icons.
- Dashboard metrics.
- Navigation structure.
- Specialized chart colors.
- Application-specific components.

A financial application and an audit platform should feel related without appearing to be the same product.

## 18.3. Accent Color Policy

The default accent remains Steel Blue.

An application may introduce a secondary accent when its domain benefits from a distinct identity. The accent should not replace semantic colors or reduce accessibility.

Keep the core visual system recognizable across all projects.

---

# 19. Anti-Patterns

The following patterns conflict with the intended identity.

### Excessive Decoration
Avoid unnecessary gradients, glows, decorative shapes, and oversized illustrations.

### Overuse of Cards
Not every section requires a card. Use spacing and headings to organize content when a separate surface adds no value.

### Excessive Color
Avoid giving every metric, chart, button, or navigation item its own accent color.

### Heavy Shadows
Do not use strong shadows as the default method of separating content.

### Inconsistent Radius
Avoid mixing unrelated corner radii throughout the same interface.

### Typography Without Hierarchy
Do not use the same size and weight for every heading, or bold every important-looking label.

### Inconsistent Status Meaning
Never reuse a semantic color for a conflicting meaning without a clearly defined reason.

### Unnecessary Animation
Avoid continuous motion, dramatic transitions, and decorative effects that do not improve usability.

### Generic Dashboard Composition
Do not create dashboards by placing a row of colorful metric cards above unrelated charts and tables without a clear information hierarchy.

---

# 20. Design Quality Checklist

Before considering a page complete, verify the following.

## Visual Consistency
- [ ] The page uses the established color tokens.
- [ ] Typography follows the defined hierarchy.
- [ ] Spacing is consistent.
- [ ] Card geometry is standardized.
- [ ] Borders and shadows are restrained.
- [ ] Interactive accents are used selectively.

## Component Quality
- [ ] Cards have a clear purpose.
- [ ] Primary actions are easy to identify.
- [ ] Tables remain readable at realistic data densities.
- [ ] Forms provide clear labels and feedback.
- [ ] Status indicators use consistent meanings.
- [ ] Empty states provide useful guidance.

## Interaction Quality
- [ ] Hover and focus states are defined.
- [ ] Keyboard navigation works.
- [ ] Disabled and loading states are understandable.
- [ ] Destructive actions are clearly identified.
- [ ] Motion remains subtle and purposeful.

## Accessibility and Responsiveness
- [ ] Text contrast is sufficient.
- [ ] Focus indicators are visible.
- [ ] Color is not the only source of information.
- [ ] Layouts work on narrow screens.
- [ ] Reduced-motion preferences are respected.
- [ ] Dark mode has been checked independently.

## Brand Independence
- [ ] No proprietary company branding is present.
- [ ] The application can use its own name and logo.
- [ ] Customization does not compromise the shared design language.
- [ ] The interface remains appropriate for multiple business domains.

---

# 21. Final Design Statement

Django Enterprise — Premium Minimal is a design system for dependable software that values clarity, consistency, and restraint.

It combines the structured character of enterprise interfaces with the refinement of minimalist product design.

Its identity comes from:
- A disciplined navy and steel-blue palette.
- Clean neutral surfaces.
- Detailed but restrained information cards.
- Carefully structured typography.
- Consistent forms and data tables.
- Subtle borders and controlled spacing.
- Functional interactions and accessible states.
- A flexible architecture for independent applications.

The ultimate objective is not to make every application look identical.

It is to ensure that every application built on this visual foundation feels considered, professional, and coherent—while retaining the freedom to express its own purpose and identity.

**Design principle:** Build interfaces that feel effortless because every detail has been considered.

---
name: Cognitive Enterprise
colors:
  surface: '#f8f9ff'
  surface-dim: '#cbdbf5'
  surface-bright: '#f8f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#eff4ff'
  surface-container: '#e5eeff'
  surface-container-high: '#dce9ff'
  surface-container-highest: '#d3e4fe'
  on-surface: '#0b1c30'
  on-surface-variant: '#444651'
  inverse-surface: '#213145'
  inverse-on-surface: '#eaf1ff'
  outline: '#757682'
  outline-variant: '#c5c5d3'
  surface-tint: '#4059aa'
  primary: '#00236f'
  on-primary: '#ffffff'
  primary-container: '#1e3a8a'
  on-primary-container: '#90a8ff'
  inverse-primary: '#b6c4ff'
  secondary: '#006c49'
  on-secondary: '#ffffff'
  secondary-container: '#6cf8bb'
  on-secondary-container: '#00714d'
  tertiary: '#5c0016'
  on-tertiary: '#ffffff'
  tertiary-container: '#850024'
  on-tertiary-container: '#ff8991'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dce1ff'
  primary-fixed-dim: '#b6c4ff'
  on-primary-fixed: '#00164e'
  on-primary-fixed-variant: '#264191'
  secondary-fixed: '#6ffbbe'
  secondary-fixed-dim: '#4edea3'
  on-secondary-fixed: '#002113'
  on-secondary-fixed-variant: '#005236'
  tertiary-fixed: '#ffdada'
  tertiary-fixed-dim: '#ffb3b6'
  on-tertiary-fixed: '#40000c'
  on-tertiary-fixed-variant: '#920028'
  background: '#f8f9ff'
  on-background: '#0b1c30'
  surface-variant: '#d3e4fe'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 60px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
    letterSpacing: -0.01em
  headline-lg-mobile:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  title-lg:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
  title-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '600'
    lineHeight: 24px
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  label-md:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
    letterSpacing: 0.05em
  code-md:
    fontFamily: Inter
    fontSize: 13px
    fontWeight: '400'
    lineHeight: 18px
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  container-margin: 24px
  gutter: 16px
  sidebar-width: 260px
---

## Brand & Style

This design system is engineered for high-utility enterprise environments, specifically focusing on employee management and resource planning. The brand personality is authoritative yet accessible, emphasizing precision, reliability, and modern efficiency. 

The aesthetic follows a **Corporate / Modern** direction. It prioritizes clarity through a structured information hierarchy, generous whitespace within high-density layouts, and a refined "Flat Plus" approach—where elements are primarily flat but utilize subtle depth cues to indicate interactivity. The emotional response should be one of "effortless control," transforming complex HR data into actionable insights.

## Colors

The palette is anchored by **Deep Indigo (#1E3A8A)**, representing stability and corporate trust. This is the primary driver for navigation, primary buttons, and brand-level elements.

- **Success & Positive States:** Emerald Green is used for "Present" statuses, "Approved" requests, and completion indicators.
- **Alert & Negative States:** Rose Red is reserved for "Absent" statuses, "Rejected" workflows, and critical system errors.
- **Neutrals:** A Slate-based neutral scale is used for typography and borders to maintain a cool, professional temperature across the interface.
- **Backgrounds:** The primary surface is a very light gray (#F8FAFC) to reduce eye strain during long working sessions, with pure white (#FFFFFF) used for content cards to create clear separation.

## Typography

The design system utilizes **Inter** exclusively. It is a systematic, utilitarian typeface designed for computer screens, making it ideal for data-heavy ERP interfaces.

- **Weight Usage:** SemiBold (600) is used for headers and titles to provide strong structural anchors. Medium (500) is used for interactive labels and buttons. Regular (400) is used for all body text and data table entries.
- **Scalability:** For mobile views, display and large headline sizes scale down significantly to ensure data remains the focal point without excessive scrolling.
- **Micro-copy:** Small labels (12px) use a slight tracking increase and uppercase styling to distinguish them from editable data.

## Layout & Spacing

The layout employs a **Fluid Grid** model with a sidebar-to-content architecture. 

- **Sidebar:** A fixed 260px left-hand navigation allows for persistent access to high-level modules (Payroll, Directory, Leave, etc.).
- **Grid:** A 12-column responsive grid is used for the main content area. In dashboard views, cards should span 3, 4, or 6 columns depending on the metric complexity.
- **Density:** We utilize a "Comfortable" density for general settings and a "Compact" density for data tables and list views. 
- **Breakpoints:**
  - **Desktop (1200px+):** Full sidebar, 12 columns.
  - **Tablet (768px - 1199px):** Collapsed sidebar (icons only), 8 columns.
  - **Mobile (<768px):** Off-canvas drawer navigation, 4 columns, vertical card stacking.

## Elevation & Depth

To maintain a modern, professional look, this design system avoids heavy shadows in favor of **Tonal Layers** and **Low-Contrast Outlines**.

- **Level 0 (Floor):** Background color (#F8FAFC).
- **Level 1 (Cards/Sidebar):** Pure white surface with a 1px border (#E2E8F0). A very soft ambient shadow (0px 1px 3px rgba(0,0,0,0.05)) is applied only to floating cards.
- **Level 2 (Dropdowns/Modals):** Increased elevation using a more distinct shadow (0px 10px 15px -3px rgba(0,0,0,0.1)) to focus user attention on the temporary task.
- **Interactivity:** On hover, interactive cards should transition from a 1px gray border to a 1px primary-colored border rather than increasing shadow depth.

## Shapes

The design system uses a **Soft (0.25rem)** roundedness approach. This creates a contemporary feel that is less aggressive than sharp corners but remains more professional and "buttoned-up" than fully rounded pill shapes.

- **Standard Elements:** Buttons, input fields, and small cards use 4px (0.25rem).
- **Large Containers:** Dashboard widgets and main content containers use 8px (0.5rem) to soften the large surface areas.
- **Status Indicators:** Small dots or badges for "Presence" may use a full circle (999px) for quick visual recognition.

## Components

### Buttons
- **Primary:** Solid Deep Indigo (#1E3A8A) with white text.
- **Secondary:** White background with 1px border (#CBD5E1) and dark slate text.
- **Ghost:** No background or border, Indigo text; used for secondary actions in tables.

### Data Tables
- **Header:** Light gray background (#F1F5F9), uppercase 12px Medium weight text.
- **Rows:** 56px minimum height, subtle 1px bottom border only. No vertical lines.
- **Selection:** Selected rows should have a light Indigo tint (#EFF6FF).

### Input Fields
- **Standard:** 1px border (#CBD5E1), 8px horizontal padding. On focus, the border changes to Primary Indigo with a 2px soft outer glow.
- **Validation:** Error states must include both a red border and a small 12px error message below the field.

### Cards & Metrics
- **Metric Cards:** Large "Title-lg" numbers with a "Label-md" description.
- **Trend Indicators:** Small Emerald (Up) or Rose (Down) text next to the metric to show period-over-period change.

### Navigation
- **Sidebar Items:** Clear icon on the left, 14px Medium text. Active state uses a vertical 4px "pill" on the far left edge and a text color shift to Primary Indigo.
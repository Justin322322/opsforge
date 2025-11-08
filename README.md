# OpsForge

A modern, static landing page for internal operations tools built with HTML, Tailwind CSS, and HTMX for progressive enhancement.

## Features

- **Modern UI**: Clean, professional design with Tailwind CSS
- **Progressive Enhancement**: HTMX for dynamic content loading without full page reloads
- **Responsive Design**: Mobile-first approach that works on all devices
- **Static Site**: No build process required - pure HTML, CSS, and JavaScript
- **GitHub Pages Ready**: Optimized for static hosting

## Tech Stack

- **HTML5**: Semantic markup
- **Tailwind CSS**: Utility-first CSS framework (via CDN)
- **HTMX 1.9.12**: Lightweight library for dynamic HTML interactions
- **Inter Font**: Premium typography from Google Fonts
- **Vanilla JavaScript**: Minimal JavaScript for enhanced interactivity

## HTMX Integration

This project uses **HTMX** for progressive enhancement, allowing dynamic content loading without JavaScript frameworks. Here's how it works:

### How HTMX is Used

HTMX enables seamless content swapping by using HTML attributes instead of JavaScript. The main patterns used in this project are:

#### 1. **Dynamic Content Loading** (`hx-get`)
Loads HTML partials from the server and injects them into the DOM:

```html
<button 
    hx-get="partials/tool-user-admin.html" 
    hx-target="#tool-dialog-content" 
    hx-swap="innerHTML">
    Open
</button>
```

#### 2. **Content Targeting** (`hx-target`)
Specifies where the loaded content should be inserted:

```html
<div id="tool-dialog-content">
    <!-- HTMX will inject content here -->
</div>
```

#### 3. **Content Swapping** (`hx-swap`)
Controls how the new content replaces existing content:

- `innerHTML`: Replaces the inner HTML of the target element
- `outerHTML`: Replaces the entire target element
- `beforebegin`: Inserts before the target element
- `afterend`: Inserts after the target element

### HTMX Features in This Project

1. **Tool Navigation**: Clicking tool cards loads detailed views via HTMX
2. **Activity Feed**: Recent activity items can load tool details dynamically
3. **Filter Buttons**: Category filters load filtered tool lists
4. **Modal/Dialog Content**: Tool details load into dialog containers

### Example HTMX Implementation

```html
<!-- In partials/activity.html -->
<button 
    class="text-xs text-brand-700 hover:text-brand-800" 
    hx-get="partials/tool-user-admin.html" 
    hx-target="#tool-dialog-content" 
    hx-swap="innerHTML">
    View
</button>

<!-- In partials/tools.html -->
<button 
    hx-get="partials/tool-feature-flags.html" 
    hx-target="#tool-dialog-content" 
    hx-swap="innerHTML">
    Open
</button>
```

### Benefits of HTMX

- **No Build Process**: Works directly with static HTML
- **Progressive Enhancement**: Falls back gracefully if JavaScript is disabled
- **Lightweight**: Much smaller than full JavaScript frameworks
- **Server-Friendly**: Works great with static file servers
- **SEO Friendly**: Content is HTML, not dynamically rendered
- **Simple**: Uses HTML attributes instead of complex JavaScript

## Getting Started

### Local Development

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Justin322322/opsforge.git
   cd opsforge
   ```

2. **Serve locally** (choose one method):

   **Option A: Python HTTP Server**
   ```bash
   # Python 3
   python -m http.server 8000
   
   # Python 2
   python -m SimpleHTTPServer 8000
   ```

   **Option B: Node.js HTTP Server**
   ```bash
   npx http-server -p 8000
   ```

   **Option C: VS Code Live Server**
   - Install the "Live Server" extension
   - Right-click `index.html` and select "Open with Live Server"

3. **Open in browser**:
   ```
   http://localhost:8000
   ```

### GitHub Pages Deployment

The project is already configured for GitHub Pages:

1. **Enable GitHub Pages**:
   - Go to repository Settings → Pages
   - Select source: `master` branch
   - Select folder: `/ (root)`
   - Click Save

2. **Access your site**:
   ```
   https://justin322322.github.io/opsforge/
   ```

3. **Auto-deployment**:
   - Any push to `master` automatically deploys
   - Changes appear within 1-2 minutes

## Customization

### Updating Content

- **Main Page**: Edit `index.html`
- **Tool Views**: Edit files in `partials/` directory
- **Styling**: Modify Tailwind classes or add custom CSS in `<style>` tags
- **Assets**: Replace files in `assets/` directory

### Tailwind Configuration

Tailwind is configured with custom brand colors. To modify:

```javascript
// In index.html <head>
tailwind.config = {
    theme: {
        extend: {
            colors: {
                brand: {
                    // Customize your brand colors
                    600: '#2563eb', // Primary brand color
                    // ... other shades
                }
            }
        }
    }
}
```

### Adding New HTMX Features

1. Create a new HTML partial in `partials/`
2. Add HTMX attributes to trigger buttons/links:
   ```html
   <button 
       hx-get="partials/your-partial.html" 
       hx-target="#target-element" 
       hx-swap="innerHTML">
       Load Content
   </button>
   ```
3. Ensure the target element exists in your HTML

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## License

This project is open source and available for use.

## Acknowledgments

- [HTMX](https://htmx.org/) - For progressive enhancement
- [Tailwind CSS](https://tailwindcss.com/) - For utility-first styling
- [Inter Font](https://fonts.google.com/specimen/Inter) - For beautiful typography

## Support

For issues, questions, or contributions, please open an issue on the GitHub repository.

---

**Built with HTMX and Tailwind CSS**


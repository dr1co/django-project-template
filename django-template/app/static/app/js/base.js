document.addEventListener("DOMContentLoaded", () => {
  // Theme toggle (the initial theme is applied by the inline script in base.html).
  const themeToggleButton = document.getElementById("theme-toggle-button");

  if (themeToggleButton) {
    themeToggleButton.addEventListener("click", () => {
      const root = document.documentElement;
      const nextTheme = root.dataset.theme === "dark" ? "light" : "dark";

      root.dataset.theme = nextTheme;

      try {
        localStorage.setItem("theme", nextTheme);
      } catch (e) {}
    });
  }

  // Off-canvas sidebar on smaller screens.
  const sidebar = document.getElementById("sidebar");
  const sidebarOverlay = document.getElementById("sidebar-overlay");
  const sidebarToggleButton = document.getElementById("sidebar-toggle-button");

  if (sidebar && sidebarOverlay && sidebarToggleButton) {
    const setSidebarOpen = (open) => {
      sidebar.classList.toggle("-translate-x-full", !open);
      sidebarOverlay.classList.toggle("hidden", !open);
      sidebarToggleButton.setAttribute("aria-expanded", String(open));
    };

    sidebarToggleButton.addEventListener("click", () => setSidebarOpen(true));
    sidebarOverlay.addEventListener("click", () => setSidebarOpen(false));

    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape") {
        setSidebarOpen(false);
      }
    });
  }

  // Collapsible sidebar menu.
  const dropdownMenuButton = document.getElementById("menu-dropdown-button");
  const dropdownList = document.getElementById("menu-dropdown-list");
  const dropdownArrow = document.getElementById("dropdown-arrow");

  if (dropdownMenuButton && dropdownList && dropdownArrow) {
    const setDropdownOpen = (open) => {
      dropdownList.classList.toggle("hidden", !open);
      dropdownArrow.classList.toggle("rotate-180", open);
      dropdownMenuButton.setAttribute("aria-expanded", String(open));
    };

    dropdownMenuButton.addEventListener("click", (e) => {
      e.stopPropagation();
      setDropdownOpen(dropdownList.classList.contains("hidden"));
    });

    // Keeps the menu open when one of its subitems is the current page.
    if (dropdownList.querySelector('[aria-current="page"]')) {
      setDropdownOpen(true);
    }
  }

  // Message alerts: manual dismiss and auto-dismiss after 5s.
  const alerts = document.querySelectorAll("[data-alert]");

  const dismissAlert = (alert) => {
    alert.style.transition = "opacity 0.2s ease";
    alert.style.opacity = "0";
    setTimeout(() => alert.remove(), 200);
  };

  alerts.forEach((alert) => {
    const dismissButton = alert.querySelector("[data-alert-dismiss]");

    if (dismissButton) {
      dismissButton.addEventListener("click", () => dismissAlert(alert));
    }
  });

  setTimeout(() => alerts.forEach(dismissAlert), 5000);
});

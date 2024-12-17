 document.addEventListener("DOMContentLoaded", () => {
  function toggleSidebar() {
    const sidebar = document.getElementById("sidebar");
    sidebar.classList.toggle("visible");
  }

  document.getElementById("menuToggle").onclick = toggleSidebar;

  function showSection(sectionId, event) {
    event.preventDefault();
    const sections = document.querySelectorAll("section");
    sections.forEach(section => {
      section.classList.remove('active');
    });
    document.getElementById(sectionId).classList.add('active');
    toggleSidebar();
  }
});

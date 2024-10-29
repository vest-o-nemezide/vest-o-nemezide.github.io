   // Ждем загрузки всего DOM
   document.addEventListener('DOMContentLoaded', () => {
    const sidebar = document.getElementById('sidebar');

    // Используем делегирование событий
    sidebar.addEventListener('mouseover', (event) => {
      const link = event.target.closest('.no-glow');
      if (link) {
        link.classList.replace('no-glow', 't-glow');
      }
    });

    sidebar.addEventListener('mouseout', (event) => {
      const link = event.target.closest('.t-glow');
      if (link) {
        link.classList.replace('t-glow', 'no-glow');
      }
    });
  });
     // Ждем загрузки всего DOM
     document.addEventListener('DOMContentLoaded', () => {
      const main = document.getElementById('main');
  
      // Используем делегирование событий
      main.addEventListener('mouseover', (event) => {
        const link = event.target.closest('.link');
        if (link) {
          link.classList.replace('link', 'glowlink');
        }
      });
  
      main.addEventListener('mouseout', (event) => {
        const link = event.target.closest('.glowlink');
        if (link) {
          link.classList.replace('glowlink', 'link');
        }
      });
    });
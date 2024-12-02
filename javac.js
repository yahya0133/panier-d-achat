const toggleButton = document.getElementById('toggle-mode');
const body = document.querySelector('.body1');
const infoCard = document.getElementById('info-card');

if (toggleButton && body) {
    const icons = {
        light: '<i class="fas fa-sun" style="color: #FFD700;"></i>', 
        dark: '<i class="fas fa-moon" style="color: #E1E1E1;"></i>'
    };

    toggleButton.addEventListener('click', () => {
        body.classList.toggle('light-mode');
        const isLightMode = body.classList.contains('light-mode');
        toggleButton.innerHTML = isLightMode ? icons.light : icons.dark;
        
    
    
    });
}
const platformInfo = {
    facebook: 'Connect Me For More Information',
    instagram:'Connect Me For More Information',
    whatsapp: 'Connect Me For More Information'
};

if (infoCard) {
    document.querySelectorAll('.icon').forEach(icon => {
        icon.addEventListener('mouseover', function() {
            const platform = Object.keys(platformInfo).find(p => this.classList.contains(p));
            
            if (platform) {
                const capitalizedPlatform = platform.charAt(0).toUpperCase() + platform.slice(1);
                infoCard.innerHTML = `
                    <p>${platformInfo[platform]}</p>
                    <h3>${capitalizedPlatform}</h3>
                    
                `;
            }
        });
    });

}

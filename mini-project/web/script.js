async function chargerDonnees() {
    const gridContainer = document.getElementById('grid');
    try {
        const response = await fetch('../scraper/data.json');
        if (!response.ok) {
            throw new Error('Erreur lors du chargement des données');
        }
        const data = await response.json();
        data.forEach(item => {
            const card = document.createElement('div');
            card.classList.add('card');
            card.innerHTML = `
                <h3>${item.title}</h3>
                <p>${item.description}</p>
            `;
            gridContainer.appendChild(card);
        });
    } catch (error) {
        console.error(error);
        gridContainer.innerHTML = '<p> Erreur du chargement des données.</p>';
    } 
}
 document.addEventListener('DOMContentLoaded', chargerDonnees);
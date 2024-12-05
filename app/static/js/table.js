function toggleEditMode() {
    const table = document.getElementById('table');
    const modeText = document.getElementById('mode-text');
    const inputs = table.querySelectorAll('.editable');
    const isEditMode = table.classList.toggle('edit-mode');

    inputs.forEach(input => input.disabled = !isEditMode);
    modeText.innerText = isEditMode ? 'Режим редактирования' : 'Режим просмотра';
}

function changeRecordsPerPage(select) {
    const value = select.value;
    window.location.href = `?records_per_page=${value}`
};

function saveData() {
    const rows = document.querySelectorAll('#table tbody tr');
    rows.forEach(row => {
        const inputs = row.querySelectorAll('.editable');
        const data = {
            id: row.cells[0].innerText.trim(), // Собираем ID из первой ячейки
        };

        // Записываем все данные из input-полей в объект
        inputs.forEach((input, index) => {
            data[`field${index + 1}`] = input.value.trim();
        });
        

        fetch('/applicants/save', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(result => {
            if (!result.success) {
                alert("Ошибка сохранения");
                //alert("Ошибка сохранения: " + result.errors.join(', '));
            }
        })
        .catch(error => alert("Произошла ошибка: " + error.message));
    });
}
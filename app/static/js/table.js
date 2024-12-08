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
    const basePath = window.location.pathname;
    rows.forEach(row => {
        const inputs = row.querySelectorAll('.editable');
        const data = {
            id: row.cells[1].innerText.trim(), // Собираем ID из первой ячейки
        };

        // Записываем все данные из input-полей в объект
        inputs.forEach((input, index) => {
            data[`field${index + 1}`] = input.value.trim();
        });
        

        fetch(`${basePath.replace(/\/$/, '')}/save`, {
            method: 'POST',
            headers: {
                'Content-Type': `application/json`
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(result => {
            if (!result.success) {
                alert("Ошибка сохранения: " + result.errors.join(', '));
            }
        })
        /*TODO : При сохрании оно летит. Почему?? */ 
        .catch(error => alert("Произошла ошибка: " + error.message));
    });
}

document.querySelector('#table').addEventListener('click', function(event) {
    const basePath = window.location.pathname;
    if (event.target.classList.contains('delete-row')) {
        const row = event.target.closest('tr');
        const id = row.cells[1].innerText.trim(); // Предполагаем, что ID в 1-й ячейке.
        fetch(`${basePath.replace(/\/$/, '')}/delete/${id}`, { method: 'DELETE' })
            .then(response => {
                if (response.ok) {
                    row.remove();
                } else {
                    alert('Ошибка при удалении строки');
                }
            })
            .catch(error => console.error('Ошибка:', error));
    }
});

document.getElementById('add-row').addEventListener('click', function () {
    const tableBody = document.querySelector('#table tbody');
    const tableHead = document.querySelector('#table thead tr');

    // Создаем новую строку
    const newRow = document.createElement('tr');

    // Добавляем кнопку удаления в первую ячейку
    const deleteCell = document.createElement('td');
    const idCell = document.createElement('td');
    deleteCell.innerHTML = '<button class="delete-row">Удалить</button>';
    newRow.appendChild(deleteCell);
    newRow.appendChild(idCell);
    

    // Создаем ячейки с input на основе заголовков таблицы
    Array.from(tableHead.cells).slice(2).forEach(() => {
        const cell = document.createElement('td');
        cell.innerHTML = `<input type="text" class="editable" value="">`;
        newRow.appendChild(cell);
    });

    // Добавляем строку в таблицу
    tableBody.appendChild(newRow);
});


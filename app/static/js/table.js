function toggleEditMode() {
    const table = document.getElementById('table');
    const modeText = document.getElementById('mode-text');
    const inputs = table.querySelectorAll('.editable');
    const isEditMode = table.classList.toggle('edit-mode');

    inputs.forEach(input => input.disabled = !isEditMode);
    modeText.innerText = isEditMode ? 'Режим редактирования' : 'Режим просмотра';
}

function changeRecordsPerPage(selectElement) {
    // Получаем текущий URL и параметры
    const url = new URL(window.location.href);
    

    // Обновляем параметр records_per_page
    url.searchParams.set('records_per_page', selectElement.value);

    // Оставляем остальные параметры (sort_by, sort_dir, search_query, page, view_mode)
    const paramsToKeep = ['sort_by', 'sort_dir', 'search_query', 'page', 'view_mode'];

    // Устанавливаем значения по умолчанию, если какого-то параметра нет
    const defaultParams = {
        sort_by: '1',          // предполагаемое значение сортировки
        page: '1',             // предполагаемая первая страница
        sort_dir: 'True',      // сортировка по умолчанию (например, по возрастанию)
        search_query: '',      // пустой запрос по умолчанию
        view_mode: 'readonly'  // режим по умолчанию
    };

    // Пробегаемся по параметрам, которые нужно оставить, и добавляем их в URL
    paramsToKeep.forEach(param => {
        if (!url.searchParams.has(param)) {
            url.searchParams.set(param, defaultParams[param] || '');  // Используем значение по умолчанию
        }
    });

    // Перенаправляем на обновленный URL
    window.location.href = url.toString();
}


function updateSearchQuery(event) {
    // Если функция вызывается из кнопки, нужно перехватить событие
    if (event) {
        event.preventDefault(); // Предотвращаем отправку формы
    }

    // Получаем значение из поля ввода
    const searchQuery = document.querySelector('input[name="search_query"]').value || '';

    // Формируем новый URL с параметрами
    const url = new URL(window.location.href);

    console.log('Текущий URL:', window.location.href); // Выводим текущий URL в консоль
    url.searchParams.set('search_query', searchQuery);

    console.log('Обновленный URL:', url.toString()); // Выводим обновленный URL в консоль

    // Если нужно, обновляем URL в адресной строке без перезагрузки страницы
    window.location.href = url.toString();
}


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

const deleteButtons = document.querySelectorAll('.delete-row');
if (deleteButtons.length > 0) {
    document.querySelector('#table').addEventListener('click', function(event) {
        if (event.target.classList.contains('delete-row')) {
            const basePath = window.location.pathname;
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
}


const addRowButton = document.getElementById('add-row');
if (addRowButton) {
    addRowButton.addEventListener('click', function () {
        const tableBody = document.querySelector('#table tbody');
        const tableHead = document.querySelector('#table thead tr');

        // Создаем новую строку
        const newRow = document.createElement('tr');

        // Добавляем кнопку удаления в первую ячейку
        const deleteCell = document.createElement('td');
        const idCell = document.createElement('td');
        deleteCell.innerHTML = '<button class="delete-row">Удалить</button>';  // добавляем кнопку удаления
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
}




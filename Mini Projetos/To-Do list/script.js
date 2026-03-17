const todoInput = document.getElementById('todoInput');
const addBtn = document.getElementById('addBtn');
const todoList = document.getElementById('todoList');
const taskCount = document.getElementById('taskCount');
const clearAllBtn = document.getElementById('clearAllBtn');

let todos = [];

function loadTodos() {
    const storedTodos = localStorage.getItem('todos');
    if (storedTodos) {
        todos = JSON.parse(storedTodos);
        renderTodos();
    }
}

function saveTodos() {
    localStorage.setItem('todos', JSON.stringify(todos));
}

function updateTaskCount() {
    const activeCount = todos.filter(todo => !todo.completed).length;
    taskCount.textContent = `${activeCount} task${activeCount !== 1 ? 's' : ''}`;
}

function renderTodos() {
    todoList.innerHTML = '';
    
    if (todos.length === 0) {
        todoList.innerHTML = `
            <div class="empty-state">
                <span>📝</span>
                <p>Nenhuma tarefa, Adicione alguma!</p>
            </div>
        `;
    } else {
        todos.forEach((todo, index) => {
            const li = document.createElement('li');
            li.className = `todo-item ${todo.completed ? 'completed' : ''}`;
            li.innerHTML = `
                <div class="checkbox" onclick="toggleTodo(${index})"></div>
                <span class="todo-text">${escapeHtml(todo.text)}</span>
                <button class="delete-btn" onclick="deleteTodo(${index})">×</button>
            `;
            todoList.appendChild(li);
        });
    }
    
    updateTaskCount();
}

function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

function addTodo() {
    const text = todoInput.value.trim();
    
    if (text === '') {
        todoInput.style.animation = 'shake 0.5s ease';
        setTimeout(() => {
            todoInput.style.animation = '';
        }, 500);
        return;
    }
    
    todos.push({
        text: text,
        completed: false
    });
    
    saveTodos();
    renderTodos();
    todoInput.value = '';
    todoInput.focus();
}

function toggleTodo(index) {
    todos[index].completed = !todos[index].completed;
    saveTodos();
    renderTodos();
}

function deleteTodo(index) {
    todos.splice(index, 1);
    saveTodos();
    renderTodos();
}

function clearAll() {
    if (todos.length === 0) return;
    
    if (confirm('Você quer mesmo deletar todas as tarefas?')) {
        todos = [];
        saveTodos();
        renderTodos();
    }
}

addBtn.addEventListener('click', addTodo);

todoInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        addTodo();
    }
});

clearAllBtn.addEventListener('click', clearAll);

const style = document.createElement('style');
style.textContent = `
    @keyframes shake {
        0%, 100% { transform: translateX(0); }
        25% { transform: translateX(-5px); }
        75% { transform: translateX(5px); }
    }
`;
document.head.appendChild(style);

loadTodos();


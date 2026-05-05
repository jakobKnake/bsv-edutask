describe('R8UC 1-3', () => {

    let email;

    before(function () {
        cy.fixture('../../test/gui/fixtures/user.json').then((user) => {
            cy.request({
                method: 'POST',
                url: 'http://localhost:5000/users/create',
                form: true,
                body: user
            }).then((response) => {
                email = user.email;
            });
        });
    });

    beforeEach(function () {
        cy.visit('http://localhost:3000');
        cy.get('[name="email"]').type(email);
        cy.get('form').submit(); 
        
        cy.get('input[placeholder="Title of your Task"]').type('New Task');
        cy.get('input[value="Create new Task"]').click();

        cy.get('.container-element a').contains('New Task').click();
    });

    // R8UC1: Create To-do
    it('Add button is disabled for empty input', () => {

        cy.get('input[placeholder*="Add a new todo item"]').clear();

        cy.get('input[type="submit"]').should('be.disabled');
    });

    it('The new active to-do item is added to the bottom of the list', () => {
        const todoText = "Buy printing paper";

        cy.get('input[placeholder*="Add a new todo item"]').type(todoText);

        cy.get('.popup-inner').find('input[type="submit"]').click();
        cy.contains('.todo-list li.todo-item', todoText, { timeout: 10000 }).should('be.visible');

        cy.get('.todo-list li.todo-item').last().should('contain.text', todoText);
    });

    /*
    //R8UC2: Toggle To-do
    it('Item is struck through', () => {

    })

    it('The item is not struck through anymore', () => {

    })*/
    
    //R8UC3: Delete To-do
    //Most likely a bug which prohibits the process of clicking desired element
    it('Todo item is removed from the todo list', () => {
        const todoText = 'Buy printing paper';
    
        cy.get('input[placeholder*="Add a new todo item"]')
        .click('top')
        .type(todoText);
        
        cy.get('.popup-inner').find('input[type="submit"]').click();

        cy.contains('.todo-list li.todo-item', todoText).should('be.visible');

        cy.contains('.todo-item', todoText)
        .find('.remover') 
        .click();

        cy.contains('.todo-list li.todo-item', todoText).should('not.exist');
        })


})

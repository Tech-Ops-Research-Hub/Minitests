// In Javascript, functions declaration,functions expressions,and immediately invoked functions expression (IIFE) are ways to define and use functions. Here's a brief overview of each:

// Function Declaration
// A function declaration defines a named function that can be called later in the code. Function declarations are hoisted, meaning they can be called before they are defined in the code.
function greet(name) {
    return "Hello, " + name + "!";
}

console.log(greet("Alice")); // Output: Hello, Alice!


//Key Features of Function Declarations
// - Hoisting: Can be called before they are defined. Fully hoised (both declaration and definition), so it can be called before the definition of the code.
// - Named: Must have a name, which is used to call the function. (e.g ...myFunction()...)
// - Scope: Have their own scope, meaning variables defined within the function are not accessible outside of it.
// - Use Cases: Ideal for defining functions that will be used multiple times throughout the code.

// Function Expression
// A function expression defines a function that can be assigned to a variable. Function expressions are not hoisted, meaning they cannot be called before they are defined.
const greet = function(name) {
    return "Hello, " + name + "!";
};

console.log(greet("Bob")); // Output: Hello, Bob!

// Key Features of Function Expressions
// - Not Hoisted: Cannot be called before they are defined.
// - Anonymous: Can be anonymous (no name) or named.
// - Scope: Have their own scope, similar to function declarations.
// - Use Cases: Useful for creating functions on the fly, especially as arguments to other functions.

// Immediately Invoked Function Expression (IIFE)
// A function expression that is defined and executed immediately after its creation. IIFEs are often used to create a new scope and avoid polluting the global namespace.
(function() {
    console.log("Hello, World!");
})(); // Output: Hello, World!

// Key Features of IIFEs
// - Immediate Execution: Runs once,right after definition.
// - Not Hoisted: Cannot be called before they are defined.
// - Isolated Scope: Creates a private scope, preventing variable leakage into the global scope.
// - Use Cases: Commonly used for initialization code or to create a private scope for variables and functions.


// When to Use Each
//Function Declaration: For reusable, named functions in a clear, hoisted context. 
//Function Expression: For functions as values (e.g.. callbacks, object methods) or when you need to control when the function is defined.
//IIFE: For creating isolated scopes, avoiding global namespace pollution, or running initialization code immediately.
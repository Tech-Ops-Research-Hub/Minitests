// for(let i=1; i<=10; i++){
//     if(i%2===0){
//         continue;
//     }
//     console.log(i);
// let x = 0;
// while (x < 3) {
//   if (x === 1) break;
//   console.log(x);
//   x++;
// }
// for (let i = 0; i < 3; i++) {
//   if (i === 2) continue;
//   console.log(i);
// }

// The Javascript engine and event loop are fundamental compenents that enable asynchronous programming and efficient execution of code in a non-blocking manner.

//Role of the Javascript Engine
// The Javascript engine is responsible for executing Javascript code. It performs several key functions: It interpretes and compiles the code into machine readable instructions, manages memory,handles the execution of functions and statements.

//Key Components of the Javascript Engine
// Call Stack: The call stack is a data structure that keeps track of function calls. When a function is invoked, it is added to the top of the stack, and when it completes, it is removed from the stack. This helps manage the execution context and ensures that functions are executed in the correct order.

//-- Tracks the execution context of functions. It follows the Last-In-First-Out (LIFO) structure, pushing new function calls and popping them when completed.
//Heap: A memory area used for dynamic memory allocation. Objects and variables are stored in the heap, and the engine manages memory allocation and garbage collection to free up unused memory. A memory area where objects, strings, and other data are stored and managed by the engine's garbage collector.

//Event Loop: The event loop is a mechanism that allows Javascript to perform non-blocking operations. It continuously checks the call stack and the task queue (or callback queue) for pending tasks. If the call stack is empty, it takes the first task from the task queue and pushes it onto the call stack for execution. This enables asynchronous operations, such as handling events, making network requests, and executing timers, without blocking the main thread.

//Compiler/Interpreter; Converts Javascript code into excutable bytecode or machine code (.g V8 Engine in chrome uses JIT compilation)

//Example; When you run let x=5; function add () {return x + 1;}, the engine allocates memory in the heap for x and add, and the call stack executes add () when called. 
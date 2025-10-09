/// In javascript we can handle errors using try, catch and finally blocks. Is managed using the try....catch statements, which allows you to handle execeptions (errors) gracefully. 
//You can also use the throw statements to create custom errors. 

//Try...catch
//The try...catch statement is used to handle errors that occur in a block of code. If an error occurs in the try block, control is passed to the catch block to handle the error.

//Syntax
try {
  // Code that may throw an error
} catch (error) {
  // Code to handle the error
}
finally {
  // Code that will always execute, regardless of whether an error occurred or not
}

//try block: Contains code that might throw an error.
//catch block: Executes if an error occurs in the try block. The error parameter contains details about the error (e.g error.message.error.name)
//finally block: Optional. Executes after the try and catch blocks, regardless of whether an error occurred or not. It's often used for cleanup tasks.

//Throw statement
//The throw statements lets you to create custom errors. You can throw any value (e.g a string, number, or object), but it's common to throw an Error object for consistency. 

//Syntax
throw expression;

//Example
function divide(a, b) {
    try{
        if (b === 0) {
            throw new Error("Division by zero is not allowed.");
        }
        return a / b;
    } catch (error){
        console.log("Error: " + error.message);
        return null;
    }
    }

    //console.log(divide(10, 2)); // Output: 5
    console.log(divide(10, 0    )); // Output: Error: Division by zero is not allowed. null


    //Types Of Errors 
    //Javascript has several built - errors types, including;

    //Errors; Generic Error
    //SyntaxError; Invalid JavaScript syntax
    //ReferenceError; Refers to a non -existent variable
    //TypeError; Incorrect type usage (e.g calling a non - function)
    //RangeError: Value out of range (e.g invalid array length)

    try {
        let x = undefinedVariable; // This will throw a ReferenceError
    } catch (error) {
        console.log (error.name, error.message)
    } // Output: ReferenceError undefinedVariable is not defined

//Summary 
//Use try...catch to handle errors gracefully
//Use throw to create custom errors 
//The finally block runs regardless of errors 
//Handle specific errors and avoid silent failures
//For asynchronous code, wrap await calls in try...catch within async functions
// Rules Summary 

// o params > ()
// 1 param > param =>(no parens)
// 2+ params > (p1, p2,....) => 
// Rest > (...p)=> (must be last)
// Destructing: ({x,y})=> x+y or ([a,b]) => a * b 
// Defaults: (x = 1) => x*2
// Invalid: line break after param without parens: x => SyntaxError : Use (x) => x or x => x on one line


// Lexical 
//Lexical - Refers to scope determined by code structure at write time, not runtime call site.
// Lexical scope : variable resolved in nested function structure where defined 

    function outer (){
        const x=10;
        function inner(){
            console.log(x); //10 - lexically inside outer
        }
        inner();
    }

    //Lexical this in arrow functions: this captured from surrounding scope at definition, fixed statically

    const obj ={
        method() {
            setTimeout(()=> { 
                console.log(this); //obj-lexically bound
            });
        }
    };

    //contrast dynamic scope: this depends on how function called (call,apply,object method). Arrow functions reject dynamic; enforce lexical

    //Lexical = source code position determines binding
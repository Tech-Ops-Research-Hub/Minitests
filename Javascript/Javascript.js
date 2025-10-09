/// To convert the string "50" into a number without using parseInt or Number, you can use the unary plus operator (+) like this:
/// let str = "50";
/// let num = +str; // num will be 50 as a number
/// console.log(typeof num); // "number"
/// This method is concise and effectively converts the string to a number.

/// Alternatively, you can also use the multiplication operator (*) with 1:
/// let str = "50";
/// let num = str * 1; // num will be 50 as a number
/// console.log(typeof num); // "number"
/// Both methods are commonly used for this purpose in JavaScript.
/// Note: The unary plus operator and multiplication method will return NaN if the string cannot be converted to a valid number.


/// Example:
/// let str = "abc";
/// let num = +str; // num will be NaN
/// console.log(typeof num); // "number"

/// let str = "abc";
/// let num = str * 1; // num will be NaN
/// console.log(typeof num); // "number"

/// Always ensure that the string represents a valid number before using these methods for conversion.


// console.log ("10"-5 + "5")
// console.log(typesof ("10"-5 + "5"))

try{
    let a=10;
    let b=0;
    if(b===0) throw("cannot be divided by zero");
    console.log(a/b);
}
catch(err){
    console.log("error",err);
}
// const signinBtn = document.querySelector('.signinBtn');
// const signupBtn = document.querySelector('.signupBtn');
// const formbx = document.querySelector('.formbx');
// const body = document.querySelector('body');

// signinBtn.onclick = function(){
//     formbx.classList.add('active')
//     body.classList.add('active')
// }

// signupBtn.onclick = function(){
//     formbx.classList.remove('active')
//     body.classList.remove('active')
// }

//FIRST NAME

let fnameInput = document.getElementById("fname");
let fnameError = document.getElementById("fname-error");
let fnameEmpty = document.getElementById("empty-fname");

//LAST NAME

let lnameInput = document.getElementById("lname");
let lnameError = document.getElementById("lname-error");
let lnameEmpty = document.getElementById("empty-lname");

//ADDRESS

let addInput = document.getElementById("add");
let addEmpty = document.getElementById("empty-add");

//PHONE

let moInput = document.getElementById("mobile");
let moError = document.getElementById("mobile-error");
let moEmpty = document.getElementById("empty-mobile");

//EMAIL

let emailInput = document.getElementById("email");
let emailError = document.getElementById("email-error");
let emailEmpty = document.getElementById("empty-email");

//PASSWORD

let passInput = document.getElementById("pass");
let passError = document.getElementById("pass-error");
let passEmpty = document.getElementById("empty-pass");

//SUBMIT

let submitBtn = document.getElementById("submitBtn");

//VALID

let validCls = document.getElementsByClassName("valid");
let invalidCls = document.getElementsByClassName("error");

//PASSWORD VERFICATION

const passVerify = (password) => {
  const regex = /^(?=.+[a-z])(?=.+[0-9])(?=.+[\$\%\^\&\!\@\#\*\(\)\<\>\?\-\_])/;
  
  return regex.test(password) && password.length >= 8;
};

//TEXT VERIFICATION (if input contain only text)

const textVerify = (text) => {
  const regex = /^[a-zA-Z]{3,}$/;

  return regex.test(text);
};

//PHONE NUMBER VERIFICATION

// const moVerify = (mobile) => {
//   const regex = /^[0-9]{10}$/;

//   return regex.test(mobile);
// };

//EMAIL VERIFICATION

const emailVerify = (email) => {
  const regex = /^[a-z0-9_]+@[a-z]{3,}\.[a-z\.]{3,}$/;

  return regex.test(email);
};

//EMPTY INPUT 

const emptyUpdate = (
  inputReference,
  emptyErrorReference,
  otherErrorReference
  ) => {
    if(!inputReference.value){
      //input is empty
      emptyErrorReference.classList.remove("hide");
      otherErrorReference.classList.add("hide");
      inputReference.classList.add("error");
    }
    else{
      //input has content
      emptyErrorReference.classList.add("hide");
    }
  };

  //ERROR STYLING AND DISPLAYING ERROR MSG

  const errorUpdate = (inputReference,errorReference) => {
    
    errorReference.classList.remove("hide");
    inputReference.classList.remove("valid");
    inputReference.classList.add("error");
  };

  //NO ERRORS

  const validInput = (inputReference) => {
    
    inputReference.classList.remove("error");
    inputReference.classList.add("valid");
  };

  //FIRST NAME

  fnameInput.addEventListener("input", () => {
    if (textVerify(fnameInput.value)) {
      //if returns true
      fnameError.classList.add("hide");
      validInput(fnameInput);
    }
    else {
      //if returns false
      errorUpdate(fnameInput,fnameError);
      //empty checker
      emptyUpdate(fnameInput,fnameEmpty,fnameError);
    }
  });

  //LAST NAME

  lnameInput.addEventListener("input", () => {
    if (textVerify(lnameInput.value)) {
      //if returns true
      lnameError.classList.add("hide");
      validInput(lnameInput);
    }
    else {
      //if returns false
      errorUpdate(lnameInput,lnameError);
      //empty checker
      emptyUpdate(lnameInput,lnameEmpty,lnameError);
     }
  });
   
  //PHONE
  // moInput.addEventListener("input", () => {
  //   if(moVerify(moInput.value)){
  //       moError.classList.add("hide");
  //       validInput(moInput);
  //   }
  //   else{
  //       errorUpdate(moInput,moError);
  //       emptyUpdate(moInput,moEmpty,moError);
  //   }
  // });

  //EMAIL

  emailInput.addEventListener("input", () => {
    if(emailVerify(emailInput.value)){
        emailError.classList.add("hide");
        validInput(emailInput);
    }
    else{
        errorUpdate(emailInput,emailError);
        emptyUpdate(emailInput,emailEmpty,emailError);
    }
  });

  //PASSWORD

  passInput.addEventListener("input", () => {
    if(passVerify(passInput.value)){
        passError.classList.add("hide");
        validInput(passInput);
    }
    else{
        errorUpdate(passInput,passError);
        emptyUpdate(passInput,passEmpty,passError);
    }
  });

  //ADDRESS

  // addInput.addEventListener("input", () => {
  //   if (textVerify(addInput.value)) {
  //     //if returns true
      
  //     validInput(fnameInput);
  //   }
  //   else {
  //     //if returns false
  //     //empty checker
  //     emptyUpdate(addInput,addEmpty);
  //   }
  // });

  //SUBMIT

  submitBtn.addEventListener("click", () => {
    if(validCls.length == 5 && invalidCls.length == 0){
        alert("Registration Successfull...");
    }
    else{
        alert("Error, Please try again...")
    }
  });
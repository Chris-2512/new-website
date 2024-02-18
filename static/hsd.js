const firebaseConfig = {
  apiKey: "AIzaSyDbRV_S-zMjO0ywnr1-s-VcDhG4VjTAVJw",
  authDomain: "hsd-web.firebaseapp.com",
  databaseURL: "https://hsd-web-default-rtdb.firebaseio.com",
  projectId: "hsd-web",
  storageBucket: "hsd-web.appspot.com",
  messagingSenderId: "295910268761",
  appId: "1:295910268761:web:c737a14fcfcfa7bf3c7648"
};

// Initialize firebase
firebase.initializeApp(firebaseConfig);

// Reference for db
var hsdDB = firebase.database().ref("hsd");

document.getElementById('1').addEventListener('submit', submitForm);

function submitForm(event) {
  event.preventDefault();

  var name = document.getElementById('name').value;
  var email = document.getElementById('Email').value;
  var comment = document.getElementById('Comment').value;
  var URL = document.getElementById('URL').value;
  console.log(name, email, comment, URL);
  saveComment(name, email, comment, URL);
  document.getElementById("1").reset();
}

const saveComment = (name, email, comment, URL) => {
  var newhsd = hsdDB.push();
  newhsd.set({
    name: name,
    email: email,
    comment: comment,
    URL: URL
  });
};

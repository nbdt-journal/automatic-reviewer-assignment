// Import the functions you need from the SDKs you need
//import { initializeApp } from "firebase/app";
//import { getAnalytics } from "firebase/analytics";


// Import the functions you need from the SDKs you need
import { initializeApp, getApp, getApps } from 'firebase/app'
import { getFirestore } from 'firebase/firestore'
import { getAuth } from 'firebase/auth'
//import { getAnalytics } from "firebase/analytics";

// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyB99axyvn-PMlJJTskExuRnk1MRhoCONY4",
  authDomain: "automatic-reviewer-assignment.firebaseapp.com",
  projectId: "automatic-reviewer-assignment",
  storageBucket: "automatic-reviewer-assignment.appspot.com",
  messagingSenderId: "237987232431",
  appId: "1:237987232431:web:381548035f551b98f5f25a",
  measurementId: "G-R0CBWNEYHP"
};

// Initialize Firebase
//const app = initializeApp(firebaseConfig);
//const analytics = getAnalytics(app);

// Initialize Firebase
const app = !getApps().length ? initializeApp(firebaseConfig) : getApp()
const db = getFirestore()
const auth = getAuth()
//const analytics = getAnalytics(app);

export default app
export { auth, db }
// ----------------------------------- FIREBASE CONFIGURATION -----------------------------------------
var firebaseConfig = {
    apiKey: "AIzaSyAbHTO3Ufs5rI6QXS4MKMEoqQ7ei6gHiUU",
    authDomain: "sharemarketindex-2efa1.firebaseapp.com",
    databaseURL: "https://sharemarketindex-2efa1-default-rtdb.asia-southeast1.firebasedatabase.app",
    projectId: "sharemarketindex-2efa1",
    storageBucket: "sharemarketindex-2efa1.appspot.com",
    messagingSenderId: "722529550315",
    appId: "1:722529550315:web:83ee0f88a5ca4d2833a3ae",
    measurementId: "G-TTX4S7FNRR",
    databaseURL: "https://sharemarketindex-2efa1-default-rtdb.asia-southeast1.firebasedatabase.app/"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);

// ---------------------------------------- GET DATA FROM FIREBASE -------------------------------------
function selectAllData(){
    firebase.database().ref('Companies Info').once('value',
    function(AllRecords){
        AllRecords.forEach(
            function(CurrentRecord){
                var CompanyName = CurrentRecord.val().CompanyName;
                var Symbol = CurrentRecord.val().Symbol;
                var MarketPrice = CurrentRecord.val().MarketPrice;
                var EPS = CurrentRecord.val().EPS;
                var PE = CurrentRecord.val().PE;
                var Dividend = CurrentRecord.val().Dividend;
                var Bonus = CurrentRecord.val().Bonus;
                var RightShare = CurrentRecord.val().RightShare;
                var Average = CurrentRecord.val().Average;
                addItemsToTable(CompanyName,Symbol,MarketPrice,EPS,PE,Dividend,Bonus,RightShare,Average);
            }
        );
    });
}
window.onload = selectAllData;

// -------------------------- Filling the table from data -------------------
var companyNumber;
function addItemsToTable(CompanyName,Symbol,MarketPrice,EPS,PE,Dividend,Bonus,RightShare,Average){
    var tbody = document.getElementById('tbody');
    var trow = document.createElement('tr');
    var td1 = document.createElement('td');    var td2 = document.createElement('td');    var td3 = document.createElement('td');    var td4 = document.createElement('td');    var td5 = document.createElement('td');    var td6 = document.createElement('td');    var td7 = document.createElement('td');    var td8 = document.createElement('td');    var td9 = document.createElement('td');  var td10 = document.createElement('td');
    td1.innerHTML = ++companyNumber;
    td2.innerHTML = CompanyName;
    td3.innerHTML = Symbol;
    td4.innerHTML = MarketPrice;
    td5.innerHTML = EPS;
    td6.innerHTML = PE;
    td7.innerHTML = Dividend;
    td8.innerHTML = Bonus;
    td9.innerHTML = RightShare;
    td10.innerHTML = Average;

    trow.appendChild(td1);    trow.appendChild(td2);    trow.appendChild(td3);    trow.appendChild(td4);    trow.appendChild(td5);    trow.appendChild(td6);    trow.appendChild(td7);    trow.appendChild(td8);    trow.appendChild(td9);    trow.appendChild(td10);
    trow.appendChild(trow);
}
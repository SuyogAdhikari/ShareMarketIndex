var table = document.getElementById("mainTable").getElementsByTagName('tbody')[0];;

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


$(document).ready(function(){
    var ref = firebase.database().ref("Companies Info");
    var table = $('.mydatatable').DataTable({
        searching: true,
        ordering: true,
        lengthChange: true
    });

    ref.orderByChild("CompanyName").once("value", function(snapshot) {
        snapshot.forEach(function(childSnapshot) {
        var childData =  childSnapshot.val();
        var CompanyName = childData.CompanyName;
   
        if(CompanyName)
        {
            var dataSet = [childData.CompanyName,childData.Symbol,childData.Sector,childData.MarketPrice,childData.EPS,childData.PE,childData.Dividend,childData.Bonus,childData.RightShare,childData.Average];
            table.rows.add([dataSet]).draw();
        }
    });
       
})    

});  
 


 
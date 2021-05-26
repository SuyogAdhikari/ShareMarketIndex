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

var ref = firebase.database().ref("Companies Info");
var counter = 1;
var DataJSON = []
    ref.orderByChild("CompanyName").once("value", function(snapshot) {
        snapshot.forEach(function(childSnapshot) {
        var childData =  childSnapshot.val();
        var CompanyName = childData.CompanyName;
        var Symbol = childData.Symbol;
        var Sector = childData.Sector;
        var MarketPrice = parseFloat(String(childData.MarketPrice).replace(/,/g, ''));
        var EPS = childData.EPS
        var PE = childData.PE
        var Dividend = childData.Dividend;
        var Bonus = childData.Bonus;
        var RightShare = childData.RightShare;
        var Average = parseFloat(String(childData.Average).replace(/,/g, ''));
        if(CompanyName)
        {
            DataJSON.push({CompanyName,Symbol,Sector,MarketPrice,EPS,PE,Dividend,Bonus,RightShare,Average});
            addItemsToTable(childData.CompanyName,childData.Symbol,childData.Sector,childData.MarketPrice,childData.EPS,childData.PE,childData.Dividend,childData.Bonus,childData.RightShare,childData.Average);
        }
    });
       
    });  
  
    function filterAverage()
    {
        table.innerHTML ="";
        counter=1;
            DataJSON.sort(function(a, b) {
                return (a.Average) - (b.Average);
            });
            for(i=0;i<DataJSON.length;i++)
            {
                addItemsToTable(DataJSON[i].CompanyName,DataJSON[i].Symbol,DataJSON[i].MarketPrice,DataJSON[i].EPS,DataJSON[i].PE,DataJSON[i].Dividend,DataJSON[i].Bonus,DataJSON[i].RightShare,DataJSON[i].Average);
            }
    }

    function filterEPS()
    {
        table.innerHTML ="";
        counter=1;
            DataJSON.sort(function(a, b) {
                return (a.EPS) - (b.EPS);
            });
            for(i=0;i<DataJSON.length;i++)
            {
                addItemsToTable(DataJSON[i].CompanyName,DataJSON[i].Symbol,DataJSON[i].MarketPrice,DataJSON[i].EPS,DataJSON[i].PE,DataJSON[i].Dividend,DataJSON[i].Bonus,DataJSON[i].RightShare,DataJSON[i].Average);
            }
    }

    function filterPE()
    {
        table.innerHTML ="";
        counter=1;
            DataJSON.sort(function(a, b) {
                return (a.PE) - (b.PE);
            });
            for(i=0;i<DataJSON.length;i++)
            {
                addItemsToTable(DataJSON[i].CompanyName,DataJSON[i].Symbol,DataJSON[i].MarketPrice,DataJSON[i].EPS,DataJSON[i].PE,DataJSON[i].Dividend,DataJSON[i].Bonus,DataJSON[i].RightShare,DataJSON[i].Average);
            }
    }
   
    function filterMarketPrice()
    {
        table.innerHTML ="";
        counter=1;
        DataJSON.sort(function(a, b) {
            return (a.MarketPrice) - (b.MarketPrice);
        });
        for(i=0;i<DataJSON.length;i++)
        {
            addItemsToTable(DataJSON[i].CompanyName,DataJSON[i].Symbol,DATAJSON[i].Sector,DataJSON[i].MarketPrice,DataJSON[i].EPS,DataJSON[i].PE,DataJSON[i].Dividend,DataJSON[i].Bonus,DataJSON[i].RightShare,DataJSON[i].Average);
        }
    }
    
    
     
       function addItemsToTable(cName,cSymbol,cSector,cMarketPrice,cEPS,cPE,cDividend,cBonus,cRightShare,cAverage)
       {
        var row = table.insertRow(-1);
        var sn = row.insertCell(-1);
        var companyName = row.insertCell(-1);
        var Symbol = row.insertCell(-1);
        var Sector = row.insertCell(-1);
        var MarketPrice = row.insertCell(-1);
        var EPS = row.insertCell(-1);
        var PE = row.insertCell(-1);
        var Dividend = row.insertCell(-1);
        var Bonus = row.insertCell(-1);
        var RightShare = row.insertCell(-1);
        var Average = row.insertCell(-1);

        sn.innerHTML = counter++;
        companyName.innerHTML = cName;
        Symbol.innerHTML = cSymbol;
        Sector.innerHTML = cSector;
        MarketPrice.innerHTML = cMarketPrice;
        EPS.innerHTML = cEPS;
        PE.innerHTML = cPE;
        Dividend.innerHTML = cDividend;
        Bonus.innerHTML = cBonus;
        RightShare.innerHTML = cRightShare;
        Average.innerHTML = cAverage;
       }


 
$(document).ready(() => {
    
  var hyper = new Hyperbot({ timeOut: 5000, runCallBacks: true });

  hyper.log(`kingslaver`);
  console.log("checker.js loaded");
  var hyperCCSList = $("#message");
  var ccnList = $("#ccnList");
  var cvvList = $("#cvvList");
  var deadList = $("#deadList");
  var amount = $("#amount");
  var showCvv = $("#showCvv");
  var showCcn = $("#showCcn");
  var showDead = $("#showDead");
  var progressBar = $("#hyper_progress");
  var saveCvv = $("#saveCvv");
  var saveCcn = $("#saveCcn");
  saveCvv.hide();
  saveCcn.hide();

  var lista_container = $("#lista_con");
  var lista_leb = $("#lista_leb");
  var amount_container = $("#amount_container");
  cvvList.hide();
  ccnList.hide();
  deadList.hide();
  showCvv.click(()=>{
      cvvList.slideToggle();
  });
  showCcn.click(()=>{
      ccnList.slideToggle();
  });
  showDead.click(()=>{
      deadList.slideToggle();
  });

  var startbtn = $("#startbtn");
  var stopbtn = $("#stopbtn");
  stopbtn.hide();

  startbtn.click(() => {
    startbtn.html("Please wait...");
    start_hyper();
  });

  async function start_hyper(timeOut = 500) {
    var getAmount = !amount.val() ? 0.8 : amount.val();
    var getAmount = getAmount * 100;
    var site = $("#site").val();
    var tg_id = $("#tg_id").val();
    var proxy = $("#proxy").val();
    var curr = $("#curr").val();
    var linha = hyperCCSList.val();
    var linhastart = linha.split("\n");
    var total = linhastart.length;
    var ap = 0;
    var ed = 0;
    var rp = 0;
    if (!total) {
      notify.error("Please add a cc!", "", { duration: 5000 });
    }
    linhastart.forEach(function (value, index) {
      setTimeout(function () {
        $.ajax({
          url:
            './'+ curr +'?lista=' + value + '&site=' + site + '&tg_id=' + tg_id + '&proxy=' + proxy,
          type: "GET",
          async: true,
          success: function (resultado) {
             if (resultado.match("#HITS")) {
              removelinha();
              ap++;
              aprovadas(resultado);
              notify.success(resultado, "", { duration: 3000 });
            } else if (resultado.match("#LIVE")) {
              removelinha();
              ed++;
              edrovadas(resultado);
              notify.success(resultado, "", { duration: 3000 });
            } else {
              removelinha();
              rp++;
              reprovadas(resultado);

            }

            $("#totalCount").html(total);
            var fila = parseInt(ap) + parseInt(ed) + parseInt(rp);
            $("#cvvCount").html(ap);
            $("#ccnCount").html(ed);
            $("#deadCount").html(rp);
            $("#totalChecked").html(fila);
            $("#cLive2").html(ap);
            $("#cWarn2").html(ed);
            $("#cDie2").html(rp);

            var progress = (fila / total) * 100;

            if (parseInt(ap) !== 0 && progress === 100) {
              saveCvv.show();

              saveCvv.click(async () => {
                
                  var chargedData = $("#cvvList").text();
                  return hyper.saveFile({
                    fileName: "x" + ap + "HITS",
                    fileExten: "txt",
                    fileData: [
                      chargedData.replaceAll("-", "\n"),
                    ],
                    saveData: true,
                  });
                
              });
            }

            if (parseInt(ed) !==0 && progress === 100) {
              saveCcn.show();

              saveCcn.click(async () => {
              
                  var ccnData = $("#ccnList").text();

                  return hyper.saveFile({
                    fileName: "x" + ed + "LIVE",
                    fileExten: "txt",
                    fileData: [
                      ccnData.replaceAll("-", "\n"),
                    ],
                    saveData: true,
                  });
                
              });
            }

            progressBar.css({"width":`${progress.toFixed(0)+"%"}`, height:"3px"});
            progressBar.addClass("animate__animated animate__lightSpeedInLeft")
            var process =
              "processing..." +
              progress.toFixed(0) +
              "%";
            startbtn.html(process);
            startbtn.addClass(" animate__animated animate__flip ");
            if (progress === 100) {
              startbtn.css({ color: "#0d8f3b", background: "#0eab450d" });
              startbtn.html("Checking completed!");
             setTimeout(()=>{
              startbtn.html("Loading...");
             }, 1500);
             setTimeout(()=>{
                 startbtn.hide();
                 stopbtn.show();
                 stopbtn.html("Reload checker");
             }, 5500);
             stopbtn.click(()=>{
              window.location.reload();
          });  
            }
          },
        });
      }, 35e1 * index);
    });
  }
  
  function aprovadas(str) {
    cvvList.append(str + "<br>");
  }
  function reprovadas(str) {
    deadList.append(str + "<br>");
  }
  function edrovadas(str) {
    ccnList.append(str + "<br>");
  }
  function removelinha() {
    var lines = hyperCCSList.val().split("\n");
    lines.splice(0, 1);
    hyperCCSList.val(lines.join("\n"));
  }
});
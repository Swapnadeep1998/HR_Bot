document.addEventListener("DOMContentLoaded", ()=> {
    document.querySelector("#submit").disabled = true;

    document.querySelector("#text-field").onkeyup = () => {
        if(document.querySelector("#text-field").value.length > 0)
            document.querySelector("#submit").disabled = false;
        else
            document.querySelector("#submit").disabled = true;
    };

    document.querySelector("#message").onsubmit = ()=>{

        // Creating New Paragraph For Each New Message
        const para = document.createElement('div');
        const para2 = document.createElement('div'); 

        // Defining Chat Pargraphs Styling And Behaviour
        para.style.textAlign= "center";
        para.style.maxWidth ="200px";
        para.style.wordBreak = "break-all";                    
        para.style.padding = "3px";        
        para.style.position = "relative";
        para.style.float = "right";
        para.style.marginBottom = "5px";
        para.style.marginLeft = "200px"
        para.style.backgroundColor = "violet";
        para.style.border = "3px solid black";                
        para.style.borderRadius = "7px";
        para.style.display = "inline" ;             
        

        para2.style.textAlign= "center";
        para2.style.maxWidth ="200px";
        para2.style.wordBreak = "break-all";                    
        para2.style.padding = "3px";        
        para2.style.position = "relative";
        para2.style.float = "left";
        para2.style.marginBottom = "5px";
        para2.style.marginRight = "200px"
        para2.style.backgroundColor = "yellow";
        para2.style.border = "3px solid black";                
        para2.style.borderRadius = "7px";
        para2.style.display = "inline" ;


        const request = new XMLHttpRequest();
        const message = document.querySelector('#text-field').value;
        request.open('POST','/chat');
        request.onload = ()=>{
            const data = JSON.parse(request.responseText);
            para.innerHTML = document.querySelector("#text-field").value;
            para2.innerHTML = data.bot;
            document.querySelector(".container > #chat-area").append(para);
            document.querySelector(".container > #chat-area").append(para2);

            // Auto Scroll To Bottom
        chatWindow = document.getElementById('chat-area'); 
        var xH = chatWindow.scrollHeight; 
        chatWindow.scrollTo(0, xH);
        
        // Clearing Out The Text Field
        document.querySelector("#text-field").value = '';
        document.querySelector("#submit").disabled = true;
        };    
        
        const d = new FormData();
        d.append('message',message);

        request.send(d);             
        

        return false;
    };
});
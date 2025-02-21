let usernameField = document.getElementById('id_name');

usernameField.addEventListener('keyup', (e) => {
    userVal = e.target.value;
    if (userVal.length > 0) {
        fetch('/uservalidate/', {
            body: JSON.stringify({
                username: userVal,
            }),
            method: 'POST',

        }).then(res => res.json()).then(data => {
            let msg = document.querySelector('.username')
            if (data.user_name_error) {
                msg.classList.remove('hidden')
                msg.innerText = data.user_name_error.trim();


            } else {
                if (!msg.classList.contains('hidden')) {
                    msg.classList.add('hidden');
                    const uservalidated=true;
                }

            }
        })


    }


})


let pwdField = document.getElementById('id_password');
pwdField.addEventListener('keyup', (e) => {
    pwdVal = e.target.value;
    fetch('/pwdvalidate/', {
        body: JSON.stringify({ password: pwdVal })
        , method: 'POST'
    }).then(res => res.json() ).then((data) => {
        let msg=document.querySelector('.pwd');
        if (data.pwd_security_error) {
            msg.classList.remove('hidden');
            msg.innerText=data.pwd_security_error.trim();


        }else{
            if (!msg.classList.contains('hidden')){
                msg.classList.add('hidden');

            }
            
            
        }
    })

})

let rePwd=document.getElementById('id_re_password');

rePwd.addEventListener('keyup', (e) => {
    let repwd=e.target.value;
    let pwd=document.getElementById('id_password').value;
    fetch('/matchpwd/',{
        body: JSON.stringify({
            password: pwd,
            re_password: repwd
        }),
        method: 'POST'
    }).then(res=>res.json()).then((data)=>{
        let msg=document.querySelector('.repwd');

        if(data.match_error){
            msg.classList.remove('hidden');
    
        msg.innerText=data.match_error.trim();    
            
        }
        else{
            if(!msg.classList.contains('hidden')){
                msg.classList.add('hidden');

            }
            
        }

    })
    

});






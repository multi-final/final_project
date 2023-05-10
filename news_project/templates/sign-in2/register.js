document.addEventListener('DOMContentLoaded', function() {

    const inputs = document.querySelectorAll('.input');
    const labels = document.querySelectorAll('.label-txt');
  
    inputs.forEach(function(input) {
      input.addEventListener('focus', function() {
        const parent = this.parentNode;
        const label = parent.querySelector('.label-txt');
        label.classList.add('label-active');
      });
      
      input.addEventListener('blur', function() {
        const parent = this.parentNode;
        const label = parent.querySelector('.label-txt');
        if (this.value.trim() === '') {
          label.classList.remove('label-active');
        }
      });
    });
  
  });



function isSame() {
    const password1 = document.querySelector('#passwd1').value;
    const password2 = document.querySelector('#passwd2').value;
    // if (pw.length < 6 || pw.length > 16) {
    //     window.alert('비밀번호는 6글자 이상, 16글자 이하만 이용 가능합니다.');
    //     document.getElementById('pw').value=document.getElementById('pwCheck').value='';
    //     document.getElementById('same').innerHTML='';
    // }
    if(password1!='' && document.password2!='') {
        if(password1==password2) {
            document.getElementById('return').innerHTML='비밀번호가 일치합니다.';
            document.getElementById('return').style.color='#5887f7';
        }
        else {
            document.getElementById('return').innerHTML='비밀번호가 일치하지 않습니다.';
            document.getElementById('return').style.color='#fa4b4b';
        }
    }
}
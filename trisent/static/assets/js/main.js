const url=window.location.href
const searchform=document.getElementById('search-form')
const searchinput=document.getElementById('search-input')
const resultsbox=document.getElementById('results-box')
const csrf=document.getElementsByName('csrfmiddlewaretoken')[0].value
console.log(csrf)

const sendsearchdate=(game)=>{
  $.ajax({
    type:'POST',
    url:'search/',
    data:{
      'csrfmiddllewaretoken':csrf,
      'products':products
    },
    success: (res)=>{
      console.log(res)
    },
    error: (err)=>{
      console.log(err)
    }
  })
}



searchinput.addEventListener('keyup',e=>{
  console.log(e.target.value)

  if(resultsbox.classList.contains('not-visible')){
    resultsbox.classList.remove('not-visible')
  }
   sendsearchdate(e.target.value)
})
function copyFunction() {
    var copyLink = document.getElementById('{{image.id}}.url')
    /*document.getElementById(element).select();
    document.execCommand("copy");*/
    console.log('Copied')
    document.execCommand('copy')
    alert("Link Copied")
  }
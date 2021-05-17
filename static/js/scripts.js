 copyFunction = (element) => {
    /*var copyLink = document.getElementById('{{image.id}}.url')*/
    document.getElementById(element).select();

    document.execCommand("copy");
    console.log('Copied')
    alert("Link Copied")
  }

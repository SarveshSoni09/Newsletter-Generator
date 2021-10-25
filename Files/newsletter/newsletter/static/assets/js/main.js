(function() {
  "use strict";

  /**
   * Easy selector helper function
   */
  const select = (el, all = false) => {
    el = el.trim()
    if (all) {
      return [...document.querySelectorAll(el)]
    } else {
      return document.querySelector(el)
    }
  }

  /**
   * Easy event listener function
   */
  const on = (type, el, listener, all = false) => {
    let selectEl = select(el, all)
    if (selectEl) {
      if (all) {
        selectEl.forEach(e => e.addEventListener(type, listener))
      } else {
        selectEl.addEventListener(type, listener)
      }
    }
  }

  /**
   * Easy on scroll event listener 
   */
  const onscroll = (el, listener) => {
    el.addEventListener('scroll', listener)
  }

  /**
   * Navbar links active state on scroll
   */
  let navbarlinks = select('#navbar .scrollto', true)
  const navbarlinksActive = () => {
    let position = window.scrollY + 200
    navbarlinks.forEach(navbarlink => {
      if (!navbarlink.hash) return
      let section = select(navbarlink.hash)
      if (!section) return
      if (position >= section.offsetTop && position <= (section.offsetTop + section.offsetHeight)) {
        navbarlink.classList.add('active')
      } else {
        navbarlink.classList.remove('active')
      }
    })
  }
  window.addEventListener('load', navbarlinksActive)
  onscroll(document, navbarlinksActive)

  /**
   * Scrolls to an element with header offset
   */
  const scrollto = (el) => {
    let header = select('#header')
    let offset = header.offsetHeight

    if (!header.classList.contains('header-scrolled')) {
      offset -= 16
    }

    let elementPos = select(el).offsetTop
    window.scrollTo({
      top: elementPos - offset,
      behavior: 'smooth'
    })
  }

  /**
   * Header fixed top on scroll
   */
  let selectHeader = select('#header')
  if (selectHeader) {
    let headerOffset = selectHeader.offsetTop
    let nextElement = selectHeader.nextElementSibling
    const headerFixed = () => {
      if ((headerOffset - window.scrollY) <= 0) {
        selectHeader.classList.add('fixed-top')
        nextElement.classList.add('scrolled-offset')
      } else {
        selectHeader.classList.remove('fixed-top')
        nextElement.classList.remove('scrolled-offset')
      }
    }
    window.addEventListener('load', headerFixed)
    onscroll(document, headerFixed)
  }

  /**
   * Back to top button
   */
  let backtotop = select('.back-to-top')
  if (backtotop) {
    const toggleBacktotop = () => {
      if (window.scrollY > 100) {
        backtotop.classList.add('active')
      } else {
        backtotop.classList.remove('active')
      }
    }
    window.addEventListener('load', toggleBacktotop)
    onscroll(document, toggleBacktotop)
  }

  /**
   * Mobile nav toggle
   */
  on('click', '.mobile-nav-toggle', function(e) {
    select('#navbar').classList.toggle('navbar-mobile')
    this.classList.toggle('bi-list')
    this.classList.toggle('bi-x')
  })

  /**
   * Mobile nav dropdowns activate
   */
  on('click', '.navbar .dropdown > a', function(e) {
    if (select('#navbar').classList.contains('navbar-mobile')) {
      e.preventDefault()
      this.nextElementSibling.classList.toggle('dropdown-active')
    }
  }, true)

  /**
   * Scrool with ofset on links with a class name .scrollto
   */
  on('click', '.scrollto', function(e) {
    if (select(this.hash)) {
      e.preventDefault()

      let navbar = select('#navbar')
      if (navbar.classList.contains('navbar-mobile')) {
        navbar.classList.remove('navbar-mobile')
        let navbarToggle = select('.mobile-nav-toggle')
        navbarToggle.classList.toggle('bi-list')
        navbarToggle.classList.toggle('bi-x')
      }
      scrollto(this.hash)
    }
  }, true)

  /**
   * Scroll with ofset on page load with hash links in the url
   */
  window.addEventListener('load', () => {
    if (window.location.hash) {
      if (select(window.location.hash)) {
        scrollto(window.location.hash)
      }
    }
  });

  /**
   * Porfolio isotope and filter
   */
  window.addEventListener('load', () => {
    let portfolioContainer = select('.portfolio-container');
    if (portfolioContainer) {
      let portfolioIsotope = new Isotope(portfolioContainer, {
        itemSelector: '.portfolio-item',
        layoutMode: 'fitRows'
      });

      let portfolioFilters = select('#portfolio-flters li', true);

      on('click', '#portfolio-flters li', function(e) {
        e.preventDefault();
        portfolioFilters.forEach(function(el) {
          el.classList.remove('filter-active');
        });
        this.classList.add('filter-active');

        portfolioIsotope.arrange({
          filter: this.getAttribute('data-filter')
        });
        portfolioIsotope.on('arrangeComplete', function() {
          AOS.refresh()
        });
      }, true);
    }

  });

  /**
   * Animation on scroll
   */
  window.addEventListener('load', () => {
    AOS.init({
      duration: 1000,
      easing: 'ease-in-out',
      once: true,
      mirror: false
    })
  });

})()

function validateForm() {
    let x = document.getElementById("form_pwd");
    let y = document.getElementById("form_con_pwd");
    let text;
    if (x != y)
    {
        text = "Passwords don't match";
    }
    else
    {
        text = "";
    }
}

var idNums = [0,0,0,0,0,0,0,0,0];
function repeatSection(section,secNum){
    var original = document.getElementById(section);
    var clone = original.cloneNode(true);
    idNums[secNum]++;
    clone.id = section + idNums[secNum];
    switch (secNum)
    {
    case 0:
      document.getElementById(section+'-name').setAttribute('name','faculty_name'+idNums[secNum]);
      document.getElementById(section+'-desc').setAttribute('name','achievements'+idNums[secNum]);
      document.getElementById(section+'-img').setAttribute('name','high-img'+idNums[secNum]);
      break;

    case 1:
      document.getElementById(section+'-desc').setAttribute('name','milestones-desc'+idNums[secNum]);
      document.getElementById(section+'-img').setAttribute('name','milestones-img'+idNums[secNum]);
      break;

    case 2:
      document.getElementById(section+'-desc').setAttribute('name','activities-desc'+idNums[secNum]);
      document.getElementById(section+'-img').setAttribute('name','activities-img'+idNums[secNum]);
      document.getElementById(section+'-cap').setAttribute('name','activities-cap'+idNums[secNum]);
      break;

    case 3:
      document.getElementById(section+'-comp').setAttribute('name','placements-comp'+idNums[secNum]);
      document.getElementById(section+'-num').setAttribute('name','placements-num'+idNums[secNum]);
      break;

    case 4:
      document.getElementById(section+'-desc').setAttribute('name','students-desc'+idNums[secNum]);
      document.getElementById(section+'-img').setAttribute('name','students-img'+idNums[secNum]);
      break;

    case 5:
      document.getElementById(section+'-desc').setAttribute('name','events-desc'+idNums[secNum]);
      document.getElementById(section+'-img').setAttribute('name','events-img'+idNums[secNum]);
      break;

    case 6:
      document.getElementById(section+'-desc').setAttribute('name','project-desc'+idNums[secNum]);
      break;

    case 7:
      document.getElementById(section+'-desc').setAttribute('name','phds-desc'+idNums[secNum]);
      break;

    case 8:
      document.getElementById(section+'-year').setAttribute('name','results-year'+idNums[secNum]);
      document.getElementById(section+'-num').setAttribute('name','results-num'+idNums[secNum]);
      break;

    }
    var x = document.getElementById('btn-'+section);
    x.style.display = "none";
    original.parentNode.insertBefore(clone, original.nextSibling);

}

function sendArray(){
  document.getElementById('array').setAttribute('value',idNums);
}

// window.onbeforeunload = function() {
//   window.localStorage.setItem(email,$('#email').val());
//   window.localStorage.setItem(pwd, $('#pwd').val());
//   window.localStorage.setItem(conpwd, $('#con_pwd').val());
// }

// window.onload = function() {
//   var email = window.localStorage.getItem(email);
//   var pwd = localStorage.getItem(pwd);
//   var con_pwd = localStorage.getItem(con_pwd);
//   console.log(email)
//   if (email !== null) $('#email').val(email);
//   if (pwd !== null) $('#pwd').val(pwd);
//   if (con_pwd !== null) $('#con_pwd').val(con_pwd);
  
// }
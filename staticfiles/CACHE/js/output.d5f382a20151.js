let isAuthenticated=false;document.addEventListener("DOMContentLoaded",()=>{isAuthenticated=document.body.dataset.authenticated==="true";initialiseAddCaravan();initialiseEditCaravan();initialiseCarousel();initialiseFilterToggle();initialiseSelect2();initialiseRequestBooking();initialiseBookingButton();initialiseEditBookingModal();initialiseImageModal();initialiseFavouriteIcons();initialiseReviewModal();initialiseEditReviewModal();initialiseReplyToReviewModal();initialiseEditReplyModal();initialiseDeleteReviewAndReply();initialiseCurrencyChange();updatePricesOnLoad();initialiseAppearanceChange();applyThemeFromCookie();initialisePaymentDetailsUpdate();if(isAuthenticated){setInterval(checkNotifications,30000);checkNotifications();}
const notificationIcon=document.getElementById("notification-icon");if(notificationIcon){notificationIcon.addEventListener("click",()=>{const modal=new bootstrap.Modal(document.getElementById("notificationModal"));modal.show();markNotificationsAsRead();});}});function parseJSON(input){try{return input.trim()?JSON.parse(input):[];}catch(e){console.error("Error parsing JSON:",e);return[];}}
function removeDuplicates(dates){return dates.filter((value,index,self)=>index===self.findIndex((t)=>t.start_date===value.start_date&&t.end_date===value.end_date));}
function getCookie(name){let cookieValue=null;if(document.cookie&&document.cookie!==""){const cookies=document.cookie.split(";");for(let i=0;i<cookies.length;i++){const cookie=cookies[i].trim();if(cookie.substring(0,name.length+1)===name+"="){cookieValue=decodeURIComponent(cookie.substring(name.length+1));break;}}}
return cookieValue;}
function showInAppMessage(message){const messageContainer=document.getElementById("success-message-container");if(messageContainer){messageContainer.textContent=message;messageContainer.style.display="block";setTimeout(()=>{messageContainer.style.display="none";},5000);}}
function initialiseSelect2(){if(window.jQuery){$(document).ready(function(){$("select[name='amenities']").select2({placeholder:"Select amenities",allowClear:true,width:"100%",});});}else{console.error("jQuery not found: Select2 requires jQuery to function.");}}
function initialiseFilterToggle(){const toggleFiltersBtn=document.getElementById("toggle-filters");const filterForm=document.getElementById("filter-form");const amenitiesSelect=document.querySelector("select[name='amenities']");if(toggleFiltersBtn){toggleFiltersBtn.addEventListener("click",function(){const filterContainer=document.getElementById("filter-container");if(filterContainer.style.display==="none"){filterContainer.style.display="block";this.textContent="Hide Filters";}else{filterContainer.style.display="none";this.textContent="Filters";}});}
if(amenitiesSelect&&filterForm){amenitiesSelect.addEventListener("change",function(){filterForm.submit();});}}
function initialiseAddCaravan(){const calendarEl=document.getElementById("calendar");const hiddenInputEl=document.getElementById("available_dates");function parseHiddenDates(){try{return hiddenInputEl.value?JSON.parse(hiddenInputEl.value):[];}catch(e){console.error("Invalid JSON in hidden input:",e);return[];}}
function updateHiddenInput(dates){hiddenInputEl.value=JSON.stringify(removeDuplicates(dates));}
const addAmenityBtn=document.getElementById("add-amenity-btn");if(addAmenityBtn){addAmenityBtn.addEventListener("click",function(){const container=document.getElementById("amenities-container");const input=document.createElement("input");input.type="text";input.name="extra_amenity";input.placeholder="Add a new amenity";input.classList.add("form-control","mb-2");container.appendChild(input);});}
const form=document.querySelector("form");if(form){form.addEventListener("submit",function(){const amenities=document.querySelectorAll("input[name='extra_amenity']");amenities.forEach((input,index)=>{input.name=`extra_amenity_${index}`;});});}
if(calendarEl){const calendar=new FullCalendar.Calendar(calendarEl,{initialView:"dayGridMonth",selectable:true,editable:true,eventResizableFromStart:true,unselectAuto:false,longPressDelay:300,eventLongPressDelay:300,select:function(info){console.log("Date selected:",info.startStr);let dates=parseHiddenDates();let adjustedEnd=new Date(info.endStr);adjustedEnd.setDate(adjustedEnd.getDate()-1);if(!dates.some((d)=>d.start_date===info.startStr&&d.end_date===adjustedEnd.toISOString().split("T")[0])){dates.push({start_date:info.startStr,end_date:adjustedEnd.toISOString().split("T")[0],});updateHiddenInput(dates);calendar.addEvent({title:"Available",start:info.startStr,end:adjustedEnd.toISOString().split("T")[0],allDay:true,});}
calendar.unselect();},dateClick:function(info){console.log("Date tapped:",info.dateStr);let dates=parseHiddenDates();let existingIndex=dates.findIndex((d)=>d.start_date===info.dateStr);if(existingIndex===-1){dates.push({start_date:info.dateStr,end_date:info.dateStr});calendar.addEvent({title:"Available",start:info.dateStr,end:info.dateStr,allDay:true,});}else{dates.splice(existingIndex,1);calendar.getEvents().forEach((event)=>{if(event.startStr===info.dateStr)event.remove();});}
updateHiddenInput(dates);},eventDidMount:function(info){info.el.style.pointerEvents="auto";},events:parseHiddenDates(),});calendar.render();}}
function initialiseEditCaravan(){const calendarEl=document.getElementById("calendar");const hiddenInputEl=document.getElementById("available_dates");function parseHiddenDates(){try{return hiddenInputEl.value?JSON.parse(hiddenInputEl.value):[];}catch(e){console.error("Invalid JSON in hidden input:",e);return[];}}
function updateHiddenInput(dates){hiddenInputEl.value=JSON.stringify(removeDuplicates(dates));}
const addAmenityBtn=document.getElementById("add-amenity-btn");if(addAmenityBtn){addAmenityBtn.addEventListener("click",function(){const container=document.getElementById("amenities-container");const input=document.createElement("input");input.type="text";input.name="extra_amenity";input.placeholder="Add a new amenity";input.classList.add("form-control","mb-2");container.appendChild(input);});}
const form=document.querySelector("form");if(form){form.addEventListener("submit",function(){const amenities=document.querySelectorAll("input[name='extra_amenity']");amenities.forEach((input,index)=>{input.name=`extra_amenity_${index}`;});});}
if(calendarEl){const calendar=new FullCalendar.Calendar(calendarEl,{initialView:"dayGridMonth",selectable:true,editable:true,eventResizableFromStart:true,unselectAuto:false,longPressDelay:300,eventLongPressDelay:300,select:function(info){console.log("Date selected:",info.startStr);let dates=parseHiddenDates();let adjustedEnd=new Date(info.endStr);adjustedEnd.setDate(adjustedEnd.getDate()-1);if(!dates.some((d)=>d.start_date===info.startStr&&d.end_date===adjustedEnd.toISOString().split("T")[0])){dates.push({start_date:info.startStr,end_date:adjustedEnd.toISOString().split("T")[0],});updateHiddenInput(dates);calendar.addEvent({title:"Available",start:info.startStr,end:adjustedEnd.toISOString().split("T")[0],allDay:true,});}
calendar.unselect();},dateClick:function(info){console.log("Date tapped:",info.dateStr);let dates=parseHiddenDates();let existingIndex=dates.findIndex((d)=>d.start_date===info.dateStr);if(existingIndex===-1){dates.push({start_date:info.dateStr,end_date:info.dateStr});calendar.addEvent({title:"Available",start:info.dateStr,end:info.dateStr,allDay:true,});}else{dates.splice(existingIndex,1);calendar.getEvents().forEach((event)=>{if(event.startStr===info.dateStr)event.remove();});}
updateHiddenInput(dates);},eventClick:function(info){let dates=parseHiddenDates();dates=dates.filter((d)=>!(d.start_date===info.event.startStr&&d.end_date===(info.event.endStr||info.event.startStr)));updateHiddenInput(dates.length>0?dates:[]);info.event.remove();},eventDidMount:function(info){info.el.style.pointerEvents="auto";},events:parseHiddenDates(),});calendar.render();}
const editModal=document.getElementById("editCaravanModal");if(editModal){editModal.addEventListener("show.bs.modal",function(event){const button=event.relatedTarget;const id=button.getAttribute("data-id");const title=button.getAttribute("data-title");const description=button.getAttribute("data-description");const berth=button.getAttribute("data-berth");const location=button.getAttribute("data-location");const price=button.getAttribute("data-price");const amenitiesAttr=button.getAttribute("data-amenities");const modal=event.target;modal.querySelector(".modal-body #id_title").value=title;modal.querySelector(".modal-body #id_description").value=description;modal.querySelector(".modal-body #id_berth").value=berth;modal.querySelector(".modal-body #id_location").value=location;modal.querySelector(".modal-body #id_price_per_night").value=price;const amenitiesField=modal.querySelector(".modal-body #id_amenities");if(amenitiesField){const options=amenitiesField.options;const amenities=amenitiesAttr?amenitiesAttr.split(","):[];for(let i=0;i<options.length;i++){options[i].selected=amenities.includes(options[i].value);}}
modal.querySelector("#editCaravanForm").setAttribute("action","/edit/"+id+"/");});}}
function initialiseCarousel(){const carousels=[];document.querySelectorAll(".carousel").forEach(function(carousel){const instance=new bootstrap.Carousel(carousel,{interval:false,});carousels.push(instance);});carousels.forEach((carousel)=>carousel.pause());}
function initialiseImageModal(){const imageModal=document.getElementById("imageModal");const modalCarouselInner=document.getElementById("modalCarouselInner");const modalTitle=document.getElementById("imageModalLabel");if(imageModal&&modalCarouselInner&&modalTitle){imageModal.addEventListener("show.bs.modal",function(event){const button=event.relatedTarget;const carouselId=button.getAttribute("data-bs-carousel-id");const carousel=document.getElementById(carouselId);if(!carousel){console.error(`Carousel with ID ${carouselId} not found.`);return;}
const carouselItems=carousel.querySelectorAll(".carousel-item");const caravanTitle=button.closest(".list-group-item").querySelector("h2").textContent;modalTitle.textContent=caravanTitle;modalCarouselInner.innerHTML="";carouselItems.forEach((item,index)=>{const newItem=item.cloneNode(true);const icon=newItem.querySelector(".fa-up-right-and-down-left-from-center");if(icon){icon.parentNode.removeChild(icon);}
if(index===0){newItem.classList.add("active");}else{newItem.classList.remove("active");}
modalCarouselInner.appendChild(newItem);});});}}
function initialiseFavouriteIcons(){const favouriteIcons=document.querySelectorAll(".favourite-icon");favouriteIcons.forEach((icon)=>{icon.addEventListener("click",function(){const caravanId=this.getAttribute("data-caravan-id");const isFavourite=this.classList.toggle("favourite");fetch(`/listings/toggle_favourite/${caravanId}/`,{method:"POST",headers:{"Content-Type":"application/json","X-CSRFToken":getCookie("csrftoken"),},body:JSON.stringify({is_favourite:isFavourite}),}).then((response)=>{if(!response.ok){throw new Error("Network response was not ok");}
return response.json();}).then((data)=>{if(!data.success){this.classList.toggle("favourite");}}).catch((error)=>{console.error("Error:",error);this.classList.toggle("favourite");});});});}
function initialiseRequestBooking(){const requestBookingCard=document.getElementById("requestBookingCard");if(requestBookingCard){const bookNowClicked=localStorage.getItem("bookNowClicked");if(bookNowClicked){requestBookingCard.style.display="block";localStorage.removeItem("bookNowClicked");}}
const bookingForm=document.getElementById("bookingForm");if(bookingForm){bookingForm.addEventListener("submit",function(){setTimeout(function(){bookingForm.reset();},1000);});}}
function initialiseBookingButton(){const bookNowBtns=document.querySelectorAll(".book-now-btn");bookNowBtns.forEach((button)=>{button.addEventListener("click",function(){const caravanId=this.getAttribute("data-caravan-id");localStorage.setItem("bookNowClicked",true);localStorage.setItem("caravanId",caravanId);updateBookingModal(caravanId);});});}
function updateBookingModal(caravanId){fetch(`/get-caravan-details/${caravanId}/`).then((response)=>response.json()).then((data)=>{const modalBody=document.querySelector("#bookCaravanModal .modal-body");if(data.success){modalBody.innerHTML=`
                  <h5 class="title text-center">${data.title}</h5>
                  <p><strong>Owner:</strong> ${data.owner}</p>
                  <p><strong>Available Dates:</strong> ${data.available_dates}</p>
                  <form id="bookingForm" method="POST" action="/book-caravan/${caravanId}/">
                      <input type="hidden" name="csrfmiddlewaretoken" value="${data.csrf_token}">
                      <div class="container">
                          <div class="row justify-content-center">
                              <div class="col-sm-8 col-md-4 mx-auto pt-1">
                                  ${data.form_html}
                              </div>
                          </div>
                      </div>
                      <div class="text-center">
                          <button type="submit" class="btn btn-primary mb-1 btn-styles">Submit</button>
                      </div>
                  </form>
              `;}else{modalBody.innerHTML=`<p class="text-danger text-center">No caravan selected for booking.</p>`;}}).catch((error)=>console.error("Error fetching caravan details:",error));}
function initialiseEditBookingModal(){document.querySelectorAll("[id^=start_date]").forEach(function(startDateInput){const bookingId=startDateInput.id.replace("start_date","");const endDateInput=document.getElementById(`end_date${bookingId}`);if(!startDateInput||!endDateInput)return;const today=new Date().toISOString().split("T")[0];if(!startDateInput.value||new Date(startDateInput.value)<new Date(today)){startDateInput.setAttribute("min",today);}
if(!endDateInput.value||new Date(endDateInput.value)<new Date(startDateInput.value)){endDateInput.setAttribute("min",startDateInput.value);}
startDateInput.addEventListener("change",function(){endDateInput.setAttribute("min",startDateInput.value);if(new Date(endDateInput.value)<new Date(startDateInput.value)){endDateInput.value=startDateInput.value;}});endDateInput.addEventListener("change",function(){if(new Date(endDateInput.value)<new Date(startDateInput.value)){alert("End date cannot be before the start date.");endDateInput.value=startDateInput.value;}});});}
function initialiseReviewModal(){const reviewButtons=document.querySelectorAll(".leave-review-btn");reviewButtons.forEach((button)=>{button.addEventListener("click",function(){const caravanId=this.getAttribute("data-caravan-id");const modal=document.getElementById(`submitReviewModal${caravanId}`);if(!modal){console.error(`Modal with ID #submitReviewModal${caravanId} not found.`);return;}
const ratingInput=modal.querySelector(`#rating-${caravanId}`);const commentTextarea=modal.querySelector(`#comment-${caravanId}`);if(!ratingInput||!commentTextarea){console.error("Rating input or comment textarea not found.");return;}
ratingInput.value="";commentTextarea.value="";try{const bootstrapModal=new bootstrap.Modal(modal);bootstrapModal.show();}catch(error){console.error("Error initializing Bootstrap modal:",error);}});});}
function initialiseEditReviewModal(){const editReviewButtons=document.querySelectorAll(".edit-review-btn");editReviewButtons.forEach((button)=>{button.addEventListener("click",function(){const reviewId=this.getAttribute("data-review-id");const rating=this.getAttribute("data-rating");const comment=this.getAttribute("data-comment");const modal=document.querySelector(`#editReviewModal${reviewId}`);const ratingInput=modal.querySelector(`#rating-${reviewId}`);const commentTextarea=modal.querySelector(`#comment-${reviewId}`);const form=modal.querySelector(".edit-review-form");ratingInput.value=rating;commentTextarea.value=comment;form.replaceWith(form.cloneNode(true));const newForm=modal.querySelector(".edit-review-form");newForm.addEventListener("submit",function(event){event.preventDefault();const formData=new FormData(newForm);const url=newForm.getAttribute("action");handleEdit(url,formData,"Review edited successfully!");});});});}
function initialiseReplyToReviewModal(){const replyButtons=document.querySelectorAll(".reply-btn");replyButtons.forEach((button)=>{button.addEventListener("click",function(){const reviewId=this.getAttribute("data-review-id");const modal=document.querySelector(`#replyModal${reviewId}`);const replyTextarea=modal.querySelector(`#reply`);replyTextarea.value="";});});}
function initialiseEditReplyModal(){const editReplyButtons=document.querySelectorAll(".edit-reply-btn");editReplyButtons.forEach((button)=>{button.addEventListener("click",function(){const replyId=this.getAttribute("data-reply-id");const replyText=this.getAttribute("data-reply-text");const modal=document.querySelector(`#editReplyModal${replyId}`);const replyTextarea=modal.querySelector(`#reply`);const form=modal.querySelector(".edit-reply-form");replyTextarea.value=replyText;form.replaceWith(form.cloneNode(true));const newForm=modal.querySelector(".edit-reply-form");newForm.addEventListener("submit",function(event){event.preventDefault();const formData=new FormData(newForm);const url=newForm.getAttribute("action");handleEdit(url,formData,"Reply edited successfully!");});});});}
function handleEdit(url,formData,successMessage){fetch(url,{method:"POST",headers:{"X-CSRFToken":getCookie("csrftoken"),"X-Requested-With":"XMLHttpRequest",},body:formData,}).then((response)=>{if(!response.ok){return response.json().then((data)=>{if(response.status===403){throw new Error(data.error||"You are not allowed to edit this.");}else if(response.status===400){throw new Error("Invalid form submission.");}else{throw new Error("An unexpected error occurred.");}});}
return response.json();}).then((data)=>{if(data.success){showInAppMessage(successMessage);location.reload();}else{showInAppMessage(data.error||"An error occurred.");}}).catch((error)=>{console.error("Error:",error.message);showInAppMessage(error.message);});}
function initialiseDeleteReviewAndReply(){document.querySelectorAll(".delete-review-btn").forEach((button)=>{button.addEventListener("click",function(event){event.preventDefault();handleDelete(this.getAttribute("data-url"));});});document.querySelectorAll(".delete-reply-btn").forEach((button)=>{button.addEventListener("click",function(event){event.preventDefault();handleDelete(this.getAttribute("data-url"));});});}
function handleDelete(url){fetch(url,{method:"POST",headers:{"X-CSRFToken":getCookie("csrftoken"),"X-Requested-With":"XMLHttpRequest",},}).then((response)=>{if(!response.ok){return response.json().then((data)=>{if(response.status===403){throw new Error(data.error||"You do not have permission to perform this action.");}else if(response.status===404){throw new Error(data.error||"The item you are trying to delete does not exist.");}else{throw new Error("An unexpected error occurred.");}});}
return response.json();}).then((data)=>{if(data.success){location.reload();}else{showInAppMessage(data.error||"An error occurred while deleting the review.");}}).catch((error)=>{console.error("Error:",error.message);showInAppMessage(error.message);});}
function initialiseCurrencyChange(){const saveBtn=document.getElementById("save-changes-btn");if(!saveBtn)return;saveBtn.addEventListener("click",(event)=>{event.preventDefault();const form=document.getElementById("preferences-form");if(!form)return;const formData=new FormData(form);fetch(form.action,{method:"POST",body:formData,headers:{"X-CSRFToken":formData.get("csrfmiddlewaretoken"),},}).then((response)=>response.json()).then((data)=>{if(data.success){const modal=document.getElementById("editPreferencesModal");const bootstrapModal=bootstrap.Modal.getInstance(modal);bootstrapModal.hide();updatePrices(data.currency);showInAppMessage("Currency preference saved successfully.");setTimeout(()=>{location.reload();},100);}else{showInAppMessage("An error occurred while saving the currency preference.");}}).catch((error)=>{console.error("Error:",error);showInAppMessage("An error occurred while saving the currency preference.");});});}
function updatePrices(newCurrency){document.querySelectorAll(".price").forEach((priceElement)=>{const originalAmount=priceElement.dataset.amount;if(!originalAmount)return;fetch(`/listings/convert_price/?amount=${originalAmount}&currency=${newCurrency}`).then((response)=>response.json()).then((data)=>{priceElement.textContent=`${data.converted_amount} ${newCurrency}`;}).catch((error)=>{console.error("Error updating prices:",error);});});}
function updatePricesOnLoad(){const userCurrency=document.body.dataset.userCurrency;if(userCurrency){updatePrices(userCurrency);}}
function initialiseAppearanceChange(){const appearanceSelect=document.getElementById("appearance");const saveBtn=document.getElementById("save-changes-btn");if(saveBtn&&appearanceSelect){saveBtn.addEventListener("click",function(event){event.preventDefault();const newAppearance=appearanceSelect.value;const form=document.getElementById("preferences-form");if(form){const formData=new FormData(form);fetch("/user_settings/edit_preferences/",{method:"POST",headers:{"X-CSRFToken":getCookie("csrftoken"),},body:new URLSearchParams(formData),}).then((response)=>response.json()).then((data)=>{if(data.error){console.error("Error:",data.error);}else{document.body.classList.remove("light-theme","dark-theme");document.body.classList.add(`${newAppearance}-theme`);document.cookie=`theme=${newAppearance}; path=/`;document.getElementById("preferences-appearance").textContent=data.appearance;const modal=bootstrap.Modal.getInstance(document.getElementById("editPreferencesModal"));modal.hide();showInAppMessage(data.message);}}).catch((error)=>{console.error("Error:",error);showInAppMessage("An error occurred while changing the appearance.");});}else{console.error('Form with id "preferences-form" not found.');}});}}
function applyThemeFromCookie(){const theme=getCookie("theme");const isHomepage=window.location.pathname==="/";if(theme&&!isHomepage){document.body.classList.remove("light-theme","dark-theme");document.body.classList.add(`${theme}-theme`);document.querySelectorAll(".modal").forEach((modal)=>{modal.classList.remove("light-theme","dark-theme");});}}
function checkNotifications(){if(!isAuthenticated){return;}
fetch("/user_settings/get_notifications/").then((response)=>response.json()).then((data)=>{if(!data.notifications_enabled){return;}
const notificationCount=document.getElementById("notification-count");const notificationIcon=document.getElementById("notification-icon");const notificationList=document.getElementById("notifications-list");if(data.count>0){notificationCount.textContent=data.count;notificationCount.style.display="inline";notificationIcon.classList.add("flash","shake");notificationList.innerHTML="";data.notifications.forEach((notification)=>{const p=document.createElement("p");const overview=document.createElement("strong");overview.classList.add("notification-type");overview.textContent=`${notification.type}: `;const message=document.createElement("span");message.classList.add("notification-message");message.textContent=`${notification.message} (${notification.created_at})`;if(notification.link){const link=document.createElement("a");link.href=notification.link;link.textContent=" View Details";link.classList.add("notification-link");link.style.marginLeft="5px";link.target="_blank";message.appendChild(link);}
p.appendChild(overview);p.appendChild(message);notificationList.appendChild(p);});}else{notificationCount.style.display="none";notificationIcon.classList.remove("flash","shake");}}).catch((error)=>{console.error("Error fetching notifications:",error);});}
function initialisePaymentDetailsUpdate(){const paymentForm=document.querySelector("#payment-form");if(paymentForm){paymentForm.addEventListener("submit",function(event){event.preventDefault();let formData=new FormData(this);fetch(this.action,{method:"POST",body:formData,headers:{"X-CSRFToken":formData.get("csrfmiddlewaretoken")},}).then((response)=>response.json()).then((data)=>{if(data.success){const paymentDetailsSection=document.getElementById("payment-details-section");if(paymentDetailsSection){paymentDetailsSection.innerHTML=`
                <p><strong>Payment Method:</strong> ${data.payment_method}</p>
                <p><strong>Card Last Four:</strong> **** **** **** ${data.card_last_four}</p>
                <p><strong>Billing Address:</strong> ${data.billing_address}</p>
                <button type="button" class="btn btn-primary mt-3 btn-styles" data-bs-toggle="modal" data-bs-target="#editPaymentDetailsModal">
                    Edit Payment Details
                </button>`;}
const modalElement=document.getElementById("editPaymentDetailsModal");if(modalElement){const modal=bootstrap.Modal.getInstance(modalElement);if(modal){modal.hide();}}
if(data.message){showInAppMessage(data.message);}}else{showInAppMessage(data.error||"An error occurred while updating payment details.");}}).catch((error)=>{console.error("Error:",error);showInAppMessage("A network error occurred. Please try again.");});});}}
function markNotificationsAsRead(){fetch("/user_settings/mark_notifications_read/",{method:"POST",headers:{"X-CSRFToken":getCookie("csrftoken"),"Content-Type":"application/json",},body:JSON.stringify({}),}).then((response)=>response.json()).then(()=>{document.getElementById("notification-count").style.display="none";document.getElementById("notification-icon").classList.remove("flash","shake");}).catch((error)=>console.error("Error marking notifications as read:",error));}
function initialisePaymentDetailsUpdate(){const paymentForm=document.querySelector("#payment-form");if(paymentForm){paymentForm.addEventListener("submit",function(event){event.preventDefault();let formData=new FormData(this);fetch(this.action,{method:"POST",body:formData,headers:{"X-CSRFToken":formData.get("csrfmiddlewaretoken")},}).then((response)=>response.json()).then((data)=>{if(data.success){const paymentDetailsSection=document.getElementById("payment-details-section");if(paymentDetailsSection){paymentDetailsSection.innerHTML=`
                <p><strong>Payment Method:</strong> ${data.payment_method}</p>
                <p><strong>Card Last Four:</strong> **** **** **** ${data.card_last_four}</p>
                <p><strong>Billing Address:</strong> ${data.billing_address}</p>
                <button type="button" class="btn btn-primary mt-3 btn-styles" data-bs-toggle="modal" data-bs-target="#editPaymentDetailsModal">
                    Edit Payment Details
                </button>`;}
const modalElement=document.getElementById("editPaymentDetailsModal");if(modalElement){const modal=bootstrap.Modal.getInstance(modalElement);modal.hide();}
showInAppMessage(data.message||"Payment details updated successfully!");}else{showInAppMessage(data.error||"An error occurred while updating payment details.");}}).catch((error)=>{console.error("Error:",error);showInAppMessage("A network error occurred. Please try again.","error");});});}};
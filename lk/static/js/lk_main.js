
    // balance button color
    var balance = {{balance}}
    console.log(balance)
    if (balance < 0){
      $('#card_balance').removeClass( "bg-success" );
      $('#card_balance').addClass( "bg-danger" );
    }

    //payment
    function isNumber(evt) {
            evt = (evt) ? evt : window.event;
            var charCode = (evt.which) ? evt.which : evt.keyCode;
            if (charCode > 31 && (charCode < 48 || charCode > 57)) {
                return false;
            }
            return true;
        }


        function getCookie(c_name)
        {
            if (document.cookie.length > 0)
            {
                c_start = document.cookie.indexOf(c_name + "=");
                if (c_start != -1)
                {
                    c_start = c_start + c_name.length + 1;
                    c_end = document.cookie.indexOf(";", c_start);
                    if (c_end == -1) c_end = document.cookie.length;
                    return unescape(document.cookie.substring(c_start,c_end));
                }
            }
            return "";
         }


        function send_pay_prepare() {
            var confirm_sum_show = document.getElementById('payment_sum').value;
            //var Subtotal_P = document.getElementById('Subtotal_P').value;
            //var Order_IDP = document.getElementById('Order_IDP').value;
            //var Customer_IDP = document.getElementById('Customer_IDP').value;
            //var Signature = document.getElementById('Signature').value;

            if(confirm_sum_show===''){return;}
            console.log(confirm_sum_show)
            $.ajaxSetup({ headers: { "X-CSRFToken": getCookie("csrftoken"),
                                    "X-Requested-With": "XMLHttpRequest" }});
            $.ajax({
                type: "POST",
                url: "{% url 'pay_prepare' %}",
                data: {
                    'payment_sum': confirm_sum_show
                },
                dataType: 'json',
                success: function (data) {
                    console.log(data.Order_IDP)
                    $("#confirm_sum_show").text(confirm_sum_show);
                    document.getElementById('Subtotal_P').value = data.Subtotal_P;
                    document.getElementById('Order_IDP').value = data.Order_IDP;
                    document.getElementById('Customer_IDP').value = data.Customer_IDP;
                    document.getElementById('Signature').value = data.Signature;
                    $('#payConfirmModal').removeClass( "d-none" );
                    $('#payConfirmModal').modal('show');
                    //send_pay(data);
                }
            });
        };

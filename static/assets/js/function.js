$(document).ready(function () {
    $(".add-to-cart-btn").on("click", function (){
    let this_val = $(this)
    let index = this_val.attr("data-index")

    let quantity = $(".product-quantity-"+ index).val()

    let product_name = $(".product-name-"+ index).val()
    let product_image = $(".product-image-"+ index).val()
    let product_pid = $(".product-pid-"+ index).val()
    let product_price = $(".product-price-"+ index).val()



    console.log("Product Name:", product_name);
    console.log("Product PID:", product_pid);
    console.log("Product Image:", product_image);
    console.log("Quantity:", quantity);
    console.log("Product Price:", product_price);
    console.log("Current Elements:", this_val);

    $.ajax({
        url: '/add-to-cart',
        data: {
            'id': product_pid,
            'qty': quantity,
            'image': product_image,
            'title': product_name,
            'price': product_price,
        },
        dataType: 'json',
        beforeSend: function () {
            // this_val.html("✓");
            console.log("Adding product to Cart...");
        },

        success:function (response){
            this_val.html("<i class='fas fa-check-circle'></i>")
            console.log("Added Product to Cart!");

            $(".cart-count").text(response.totalcartItems)
            // this_val.attr('disabled', false)
        }
    })
    });

    $(".delete-product").on("click", function(){
        let product_id = $(this).attr("data-product")
        let this_val = $(this)

        console.log("Product ID:",  product_id);

        $.ajax({
            url: "/delete-from-cart",
            data: {
                "id": product_id
            },
            dataType: "json",
            beforeSend: function(){
                this_val.hide()
            },
            success: function(response){
                // console.log(response)
                this_val.show()
                $(".cart-items-count").text(response.totalcartitems)
                // this_val.attr('disabled',false);
                $("#cart-list").html(response.data)
                location.reload();
            }
        })
    });

    $(".update-product").on("click", function(){

        let product_id = $(this).attr("data-product")
        let this_val = $(this)
        let product_quantity = $(".product-qty-"+product_id).val()

        console.log("PRoduct ID:",  product_id);
        console.log("PRoduct QTY:",  product_quantity);

        $.ajax({
            url: "/update-cart",
            data: {
                "id": product_id,
                "qty": product_quantity,
            },
            dataType: "json",
            beforeSend: function(){
                this_val.hide()
            },
            success: function(response){
                this_val.show()
                $(".cart-items-count").text(response.totalcartitems)
                $("#cart-list").html(response.data)
                location.reload();
            }
        })
    })
})

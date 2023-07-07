//Add to card functionlity
$(document).ready(function(){
    $("#add-to-card-btn").on("click", function (){
        let quantity = $("#product-quantity").val()
        let product_name = $(".product-title").val()
        let product_id = $(".product-id").val()
        let product_price = $("#new-price").text()
        let this_val = $(this)

        console.log("Quantity:", quantity);
        console.log("Product Name:", product_name);
        console.log("Product ID:", product_id);
        console.log("Product Price:", product_price);
        console.log("Current Elements:", this_val)

        return false;
    });
});

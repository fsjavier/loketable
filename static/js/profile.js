// Add event listener to Delete Product modal
const deleteProductModal = document.getElementById('deleteProductModal')

deleteProductModal.addEventListener('show.bs.modal', event => {
    const relatedTarget = event.relatedTarget;  // Button that triggered the modal

    const productTitle = relatedTarget.getAttribute('data-product-title');
    const productID = relatedTarget.getAttribute('data-product-id');
    const productSlug = relatedTarget.getAttribute('data-product-slug');

    const productTitleElement = event.target.querySelector('#product-title');
    const formElement = event.target.querySelector('form');

    productTitleElement.textContent = productTitle;

    const deleteUrl = `/products/delete/${productID}/${productSlug}/`;

    formElement.setAttribute('action', deleteUrl);
});

// Add event listener to know when a product has been toggled

const productToggleForms = document.querySelectorAll('.product-toggle-form');

productToggleForms.forEach(function(form) {
    const checkbox = form.querySelector('.form-check-input');

    checkbox.addEventListener('change', () => {
        form.submit();
    });
});

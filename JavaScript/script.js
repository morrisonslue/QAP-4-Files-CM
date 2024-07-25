// script.js
// Description: defines a customer object for a motel business, including attributes and methods to calculate customer and stay details

/**
 * Object representing customer
 * @type {Object}
 */
let customer = {
    // Personal information
    name: "Jimmy Page",                  
    birthDate: "1944-01-09",           
    gender: "Male",                    
    email: "jimmy@ledzeppelin.com",     
    phoneNumber: "225-867-5309",       
    loyaltyMember: true,               
    
    // Booking details
    roomPreferences: ["Non-smoking", "King bed", "High floor with view"], 
    specialRequests: ["Late check-out", "Record player"], 
    paymentMethod: "Credit Card",      
    paymentStatus: "Completed",        
    
    // Customer address
    mailingAddress: {
        street: "29 Melbury Road",         
        city: "London",            
        district: "Kensington and Chelsea", 
        postalCode: "W14 8AB",         
        country: "England"              
    },
    
    // Stay details
    stayPeriod: {
        checkIn: "2024-07-20",         
        checkOut: "2024-07-25"         
    },
    
    // Emergency contact
    emergencyContact: {
        name: "Scarlett Sabet",              
        relationship: "Partner",        
        phoneNumber: "987-654-3210"    
    },
    
    // Is parking needed
    parkingRequired: true,  

    // Source of the bookin
    bookingSource: "Website",
    
    // Age calculation
    getAge: function() {
        let today = new Date();
        let birthDate = new Date(this.birthDate);
        let age = today.getFullYear() - birthDate.getFullYear();
        let monthDiff = today.getMonth() - birthDate.getMonth();
        if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < birthDate.getDate())) {
            age--;
        }
        return age;
    },
    
    // Stay calculation
    getStayDuration: function() {
        let checkInDate = new Date(this.stayPeriod.checkIn);
        let checkOutDate = new Date(this.stayPeriod.checkOut);
        let timeDiff = checkOutDate - checkInDate;
        let daysDiff = timeDiff / (1000 * 3600 * 24);
        return daysDiff;
    },
    
    // Loyalty member check
    isLoyaltyMember: function() {
        return this.loyaltyMember ? "Customer is a loyalty member." : "Customer is not a loyalty member.";
    },
    
    // Combined address
    getFullAddress: function() {
        return `${this.mailingAddress.street}, ${this.mailingAddress.city}, ${this.mailingAddress.district}, ${this.mailingAddress.postalCode}, ${this.mailingAddress.country}`;
    },
    
    // Combined booking details
    getBookingDetails: function() {
        return `Booking Source: ${this.bookingSource}\nSpecial Requests: ${this.specialRequests.join(", ")}\nPayment Status: ${this.paymentStatus}`;
    },

    // Customer summary method
    getDescription: function() {
        return `
            <p><strong>Customer Name:</strong> ${this.name}</p>
            <p><strong>Age:</strong> ${this.getAge()}</p>
            <p><strong>Gender:</strong> ${this.gender}</p>
            <p><strong>Email:</strong> ${this.email}</p>
            <p><strong>Phone Number:</strong> ${this.phoneNumber}</p>
            <p><strong>Address:</strong> ${this.getFullAddress()}</p>
            <p><strong>Room Preferences:</strong> ${this.roomPreferences.join(", ")}</p>
            <p><strong>Special Requests:</strong> ${this.specialRequests.join(", ")}</p>
            <p><strong>Payment Method:</strong> ${this.paymentMethod}</p>
            <p><strong>Payment Status:</strong> ${this.paymentStatus}</p>
            <p><strong>Check-In Date:</strong> ${this.stayPeriod.checkIn}</p>
            <p><strong>Check-Out Date:</strong> ${this.stayPeriod.checkOut}</p>
            <p><strong>Duration of Stay:</strong> ${this.getStayDuration()} days</p>
            <p><strong>Emergency Contact:</strong> ${this.emergencyContact.name} (${this.emergencyContact.relationship}) - ${this.emergencyContact.phoneNumber}</p>
            <p><strong>Loyalty Status:</strong> ${this.isLoyaltyMember()}</p>
            ${this.parkingRequired ? `<p><strong>Vehicle:</strong> ${this.vehicleDetails.make} ${this.vehicleDetails.model} (License Plate: ${this.vehicleDetails.licensePlate})</p>` : ""}
            <p><strong>Booking Source:</strong> ${this.bookingSource}</p>
        `;
    },

    // Customer description method
    getRockstarParagraph: function() {
        return `
            <p>Rock legend <strong>${this.name}</strong> has checked into our motel. At the age of ${this.getAge()}, this iconic figure from ${this.mailingAddress.city}, ${this.mailingAddress.country}, continues to inspire generations. Known for his unparalleled guitar skills, ${this.name} prefers a ${this.roomPreferences.join(", ")} room and has special requests such as ${this.specialRequests.join(" and ")}.</p>
            <p>During his stay from ${this.stayPeriod.checkIn} to ${this.stayPeriod.checkOut}, ${this.name} will be enjoying the comforts of our establishment. He is a loyal member of our motel family, and we are honored to have him.</p>
            ${this.parkingRequired ? `<p>Arriving in style with his ${this.vehicleDetails.make} ${this.vehicleDetails.model} (License Plate: ${this.vehicleDetails.licensePlate}), ${this.name} ensures every detail of his stay is rockstar-ready.</p>` : ""}
            <p>For any urgent matters, his partner ${this.emergencyContact.name} can be reached at ${this.emergencyContact.phoneNumber}. Booked through ${this.bookingSource}, ${this.name}'s stay promises to be legendary.</p>
        `;
    }
};

// Car info if parking needed
if (customer.parkingRequired) {
    customer.vehicleDetails = {
        make: "Ferrari",
        model: "GTB 275",
        licensePlate: "ZEP 1968"
    };
}

console.log(customer);
console.log("Age: " + customer.getAge());
console.log("Duration of Stay: " + customer.getStayDuration() + " days");
console.log(customer.isLoyaltyMember());
console.log("Full Address: " + customer.getFullAddress());
console.log("Booking Details:\n" + customer.getBookingDetails());

// Show in html section
document.getElementById('customer-info').innerHTML += customer.getDescription();
document.getElementById('detailed-info').innerHTML += customer.getRockstarParagraph();

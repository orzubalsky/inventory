/*
 *  ""
 *  @authors The Youngest, (youngestforever@gmail.com), 2013
 *
 */

;(function($){
    var arrow = window.arrow = new function() 
    {   
        this.scrollbarWidth;
        this.maxOpacity = 1;
        
        /* These functions are called when the document loads */
        this.init = function() 
        {       
            this.interactions();
        };  
        
        this.interactions = function()
        {
            var self = this;
            var $spectra = $('.spectrum');

            for (var i=0; i < $spectra.size(); i++)
            {
                new Spectrum($spectra.eq(i), self.maxOpacity);
            }
        }
        
    };
})(jQuery);

/* good old fashioned document-ready function call. starting js action. */
$(document).ready(function()
{   
    arrow.init();    
});
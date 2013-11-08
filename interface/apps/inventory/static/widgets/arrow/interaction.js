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
        this.count = 0;
        
        /* These functions are called when the document loads */
        this.init = function() 
        {       
            var self = this;

            self.interactions();

            $(".grp-module.grp-table").on("DOMSubtreeModified", function()
            {
                var $spectra = $('.spectrum');
                var new_count = $spectra.size();
                console.log("count: " + self.count);
                console.log("new_count: " + new_count);
                if (new_count > self.count)
                {
                    for (var i=0; i < new_count; i++)
                    {
                        if (i > self.count-2)
                        {
                            new Spectrum($spectra.eq(i), self.maxOpacity);
                        }
                    }
                    self.count = new_count;
                }
            });            
        };  
        
        this.interactions = function()
        {
            var self = this;
            var $spectra = $('.spectrum');
            console.log($spectra);
            self.count = $spectra.size();
            console.log("intial count: " + self.count);
            
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

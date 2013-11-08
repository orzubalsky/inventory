/*
 *  ""
 *  @authors The Youngest, (youngestforever@gmail.com), 2013
 *
 */

;(function($){
    var spectra = window.spectra = new function() 
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
                var $spectra = $('.spectrumContainer .handle');
                var new_count = $spectra.size();

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
            var $spectra = $('.spectrumContainer .handle');
            self.count = $spectra.size();
            
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
    spectra.init();    
});

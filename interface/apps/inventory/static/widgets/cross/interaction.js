/*
 *  ""
 *  @authors The Youngest, (youngestforever@gmail.com), 2013
 *
 */

;(function($){
    var crosses = window.crosses = new function() 
    {   
        this.count = 0;
        
        /* These functions are called when the document loads */
        this.init = function() 
        {       
            var self = this;

            self.interactions();

            // $(".grp-module.grp-table").on("DOMSubtreeModified", function()
            // {
            //     var $spectra = $('.spectrumContainer .handle');
            //     var new_count = $spectra.size();

            //     if (new_count > self.count)
            //     {
            //         for (var i=0; i < new_count; i++)
            //         {
            //             if (i > self.count-2)
            //             {
            //                 new Spectrum($spectra.eq(i), self.maxOpacity);
            //             }
            //         }
            //         self.count = new_count;
            //     }
            // });            
        };  
        
        this.interactions = function()
        {
            var self = this;
            
            var $crosses = $('.cross');

            for (var i=0; i < $crosses.size(); i++)
            {
                new Cross($crosses.eq(i));
            }            
            self.count = $crosses.size();
        }
        
    };
})(jQuery);

/* good old fashioned document-ready function call. starting js action. */
$(document).ready(function()
{   
    crosses.init();    
});

class CanvasService:

    @staticmethod
    def inject_canvas_listener(page):
       
        page.add_init_script("""
        window.__canvas_answer = null;

        const originalStrokeText = CanvasRenderingContext2D.prototype.strokeText;

        CanvasRenderingContext2D.prototype.strokeText = function(text, x, y) {
            window.__canvas_answer = text;
            return originalStrokeText.apply(this, arguments);
        };
        """)


    @staticmethod
    def get_canvas_text(page):
        
        return page.evaluate("window.__canvas_answer")
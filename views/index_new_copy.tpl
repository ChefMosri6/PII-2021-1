%rebase('base.tpl')
<section>
                
 <div>
    <h2>Home Page{{index}}</h2>
    <div class="main-text">

    </div>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Quia veniam sequi cum nulla magnam minus enim vero eos? Accusamus, consectetur assumenda totam ea quibusdam ab soluta aspernatur repellendus odit facilis.
    Lorem ipsum dolor sit amet consectetur adipisicing elit. Quia veniam sequi cum nulla magnam minus enim vero eos? Accusamus, consectetur assumenda totam ea quibusdam ab soluta aspernatur repellendus odit facilis
    Lorem ipsum dolor sit amet consectetur adipisicing elit. Quia veniam sequi cum nulla magnam minus enim vero eos? Accusamus, consectetur assumenda totam ea quibusdam ab soluta aspernatur repellendus odit facilis
    Lorem ipsum dolor sit amet consectetur adipisicing elit. Quia veniam sequi cum nulla magnam minus enim vero eos? Accusamus, consectetur assumenda totam ea quibusdam ab soluta aspernatur repellendus odit facilis
    fon
    </p>
    <figure>
    <img src="/static/Imagenes/Logorock.png" alt="Logorock">
    <figcaption>img.1.0 -Rock logo inges Band</figcaption>
    </figure>
    </div>
    <article id="secondary-text">
                
    <h3>Lorem ipsum dolor sit amet consectetur adipisicing elit. Ducimus reiciendis nam sint ab sequi numquam eos voluptatem aut beatae deserunt, est accusantium itaque facere ullam placeat voluptatum sapiente quas necessitatibus!</h3>
    </article>
    </section>
    %for row in rows:
   <ul>
       <li>{{ row[0] }}</li>
       <li>{{ row[1] }}</li>
       <li>{{ row[2] }}</li>
   </ul>
   %end

        
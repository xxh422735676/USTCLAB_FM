Theorem thm3: forall P Q:Prop,
  P/\Q ->Q.
 Proof.
 intros.
 inversion H.
 apply H1.
 Qed.
 
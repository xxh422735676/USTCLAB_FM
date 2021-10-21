Theorem thm7: forall P Q:Prop,
  (P->Q) -> P->Q.
Proof.
intros.
apply H in H0.
apply H0.
Qed.